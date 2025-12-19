#!/usr/bin/env python3
"""
Sync WKInternalsNotes DocC artifacts from a WebKit checkout.

Pipeline:
  1) Generate synthetic WKAPI symbol graph + index from UIProcess Objective-C/Swift sources.
  2) Ensure Cocoa *Private.h type pages exist (grouped by ObjC category) using the index.
  3) Update GitHub links/metadata to WebKit.revision.
  4) Ensure entry metadata blocks exist.

This script does not modify References/WebKit (read-only).
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REVISION_FILE = REPO_ROOT / "WebKit.revision"
DOCC_ROOT = REPO_ROOT / "Sources" / "WKInternalsNotes" / "Documentation.docc"
LANDING_PAGE = DOCC_ROOT / "WKInternalsNotes.md"

DEFAULT_WEBKIT_CHECKOUT = REPO_ROOT / "References" / "WebKit"
WEBKIT_COCOA_HEADERS_DIR = Path("Source/WebKit/UIProcess/API/Cocoa")

DOCC_COCOA_DIR = DOCC_ROOT / "UIProcess" / "API" / "Cocoa"

MODULE_NAME = "WKInternalsNotes"
METADATA_SECTION_TITLE = "## Metadata"
DEFAULT_STATUS_VALUE = "Draft"
LAST_REVIEWED_PREFIX = "- Last reviewed:"
LAST_UPDATED_PREFIX = "- Last updated:"
WEBKIT_REVISION_PREFIX = "- WebKit revision:"
HEADER_PATH_PREFIX = "- Header (WebKit repo-relative path):"
STATUS_PREFIX = "- Status:"
DEFAULT_TABLE_HEADER = "| Key | Value |"
DEFAULT_TABLE_SEPARATOR = "| --- | ----- |"


def _read_revision() -> str:
    if not REVISION_FILE.exists():
        raise RuntimeError(f"missing revision file: {REVISION_FILE}")
    for line in REVISION_FILE.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        return s
    raise RuntimeError(f"no revision found in: {REVISION_FILE}")


def _discover_private_header_containers(webkit_root: Path) -> list[tuple[str, str]]:
    headers_dir = webkit_root / WEBKIT_COCOA_HEADERS_DIR
    if not headers_dir.exists():
        raise RuntimeError(f"missing WebKit headers dir: {headers_dir}")

    containers: list[tuple[str, str]] = []
    for header_path in sorted(headers_dir.glob("*Private.h")):
        container = header_path.stem
        header_repo_rel = f"{WEBKIT_COCOA_HEADERS_DIR}/{header_path.name}"
        containers.append((container, header_repo_rel))
    return containers


def _header_page_template(*, container: str, revision: str, header_repo_rel: str) -> str:
    today = date.today().isoformat()
    return "\n".join(
        [
            f"# ``{MODULE_NAME}/{container}``",
            "",
            "## Purpose",
            "このヘッダに定義されている API を、追跡可能な形でまとめる。",
            "",
            METADATA_SECTION_TITLE,
            DEFAULT_TABLE_HEADER,
            DEFAULT_TABLE_SEPARATOR,
            f"| Status | {DEFAULT_STATUS_VALUE} |",
            f"| Last updated | {today} |",
            f"| WebKit revision | [`{revision}`](https://github.com/WebKit/WebKit/tree/{revision}) |",
            f"| Header (WebKit repo-relative path) | [`{header_repo_rel}`](https://github.com/WebKit/WebKit/blob/{revision}/{header_repo_rel}) |",
            "",
        ]
    )


def _normalize_newlines(lines: list[str]) -> list[str]:
    return [line if line.endswith("\n") else line + "\n" for line in lines]


def _strip_trailing_blank_lines(lines: list[str]) -> list[str]:
    trimmed = list(lines)
    while trimmed and trimmed[-1].strip() == "":
        trimmed.pop()
    return trimmed

def _extract_metadata_section(lines: list[str]) -> tuple[list[str] | None, list[str]]:
    for i, line in enumerate(lines):
        if line.rstrip("\n") != METADATA_SECTION_TITLE:
            continue

        start = i
        end = start + 1
        while end < len(lines):
            if lines[end].startswith("# "):
                break
            if lines[end].startswith("## ") and lines[end].rstrip("\n") != METADATA_SECTION_TITLE:
                break
            end += 1

        return lines[start:end], lines[:start] + lines[end:]

    return None, lines


def _extract_top_bullet_metadata(lines: list[str]) -> tuple[list[str] | None, list[str]]:
    h1_index: int | None = None
    for i, line in enumerate(lines):
        if line.startswith("# "):
            h1_index = i
            break
    if h1_index is None:
        return None, lines

    i = h1_index + 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i >= len(lines) or not lines[i].startswith("- "):
        return None, lines

    bullet_start = i
    bullet_end = bullet_start
    has_known_key = False
    while bullet_end < len(lines) and lines[bullet_end].startswith("- "):
        if (
            lines[bullet_end].startswith(STATUS_PREFIX)
            or lines[bullet_end].startswith(LAST_REVIEWED_PREFIX)
            or lines[bullet_end].startswith(LAST_UPDATED_PREFIX)
            or lines[bullet_end].startswith(WEBKIT_REVISION_PREFIX)
            or lines[bullet_end].startswith(HEADER_PATH_PREFIX)
        ):
            has_known_key = True
        bullet_end += 1

    if not has_known_key:
        return None, lines

    metadata = [f"{METADATA_SECTION_TITLE}\n"]
    metadata.extend(lines[bullet_start:bullet_end])

    # Drop a single blank line right after the bullets to avoid double blank lines.
    j = bullet_end
    if j < len(lines) and lines[j].strip() == "":
        j += 1

    remaining = lines[:bullet_start] + lines[j:]
    return metadata, remaining


def _parse_metadata_kv(lines: list[str]) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith("- "):
            item = s[2:]
            key, sep, value = item.partition(":")
            if sep and key.strip():
                pairs.append((key.strip(), value.strip()))
            continue
        if s.startswith("|") and s.endswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) < 2:
                continue
            key = cells[0]
            value = cells[1]
            if key.lower() == "key" or key == "---":
                continue
            if set(key) == {"-"}:
                continue
            if key:
                pairs.append((key, value))
            continue
    return pairs


def _build_metadata_table(pairs: list[tuple[str, str]]) -> list[str]:
    lines: list[str] = [f"{METADATA_SECTION_TITLE}\n", f"{DEFAULT_TABLE_HEADER}\n", f"{DEFAULT_TABLE_SEPARATOR}\n"]
    for key, value in pairs:
        lines.append(f"| {key} | {value} |\n")
    return lines


def _normalize_header_metadata(
    *,
    metadata_lines: list[str] | None,
    revision: str,
    header_repo_rel: str,
    today: str,
) -> list[str]:
    status_value = DEFAULT_STATUS_VALUE
    last_updated_value = today
    extra_pairs: list[tuple[str, str]] = []

    if metadata_lines is not None:
        metadata_lines = [line for line in metadata_lines if line.rstrip("\n") != METADATA_SECTION_TITLE]
        for key, value in _parse_metadata_kv(metadata_lines):
            if key == "Status":
                if value:
                    status_value = value
                continue
            if key in {"Last reviewed", "Last updated"}:
                if value:
                    last_updated_value = value
                continue
            if key in {"WebKit revision", "Header (WebKit repo-relative path)"}:
                continue
            extra_pairs.append((key, value))

    base_pairs: list[tuple[str, str]] = [
        ("Status", status_value),
        ("Last updated", last_updated_value),
        ("WebKit revision", f"[`{revision}`](https://github.com/WebKit/WebKit/tree/{revision})"),
        (
            "Header (WebKit repo-relative path)",
            f"[`{header_repo_rel}`](https://github.com/WebKit/WebKit/blob/{revision}/{header_repo_rel})",
        ),
    ]
    base_pairs.extend(extra_pairs)
    return _strip_trailing_blank_lines(_normalize_newlines(_build_metadata_table(base_pairs)))


def _move_header_metadata_to_bottom(markdown: str, *, revision: str, header_repo_rel: str) -> str:
    today = date.today().isoformat()
    lines = _normalize_newlines(markdown.splitlines(keepends=True))
    lines = _normalize_newlines([line.replace(LAST_REVIEWED_PREFIX, LAST_UPDATED_PREFIX) for line in lines])

    metadata_lines, rest = _extract_metadata_section(lines)
    if metadata_lines is None:
        metadata_lines, rest = _extract_top_bullet_metadata(rest)

    metadata_lines = _normalize_header_metadata(
        metadata_lines=metadata_lines, revision=revision, header_repo_rel=header_repo_rel, today=today
    )

    rest = _strip_trailing_blank_lines(rest)
    if rest:
        rest.append("\n")
    updated_lines = rest + metadata_lines
    return "".join(updated_lines)


def _ensure_header_scaffold(*, container: str, revision: str, header_repo_rel: str) -> None:
    header_page = DOCC_COCOA_DIR / f"{container}.h.md"
    if not header_page.exists():
        header_page.parent.mkdir(parents=True, exist_ok=True)
        header_page.write_text(
            _header_page_template(container=container, revision=revision, header_repo_rel=header_repo_rel),
            encoding="utf-8",
        )
    else:
        original = header_page.read_text(encoding="utf-8")
        updated = _move_header_metadata_to_bottom(original, revision=revision, header_repo_rel=header_repo_rel)
        if updated != original:
            header_page.write_text(updated, encoding="utf-8")

    entry_dir = DOCC_COCOA_DIR / container
    entry_dir.mkdir(parents=True, exist_ok=True)

    if next(entry_dir.iterdir(), None) is None:
        (entry_dir / ".gitkeep").touch(exist_ok=True)


def _run(cmd: list[str]) -> None:
    result = subprocess.run(  # noqa: S603
        cmd,
        cwd=str(REPO_ROOT),
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"command failed ({result.returncode}): {' '.join(cmd)}\n{result.stdout}")


def _rewrite_landing_page_headers(containers: list[str]) -> None:
    if not LANDING_PAGE.exists():
        raise RuntimeError(f"missing landing page: {LANDING_PAGE}")

    lines = LANDING_PAGE.read_text(encoding="utf-8").splitlines(keepends=True)
    header_line_index: int | None = None
    for i, line in enumerate(lines):
        if line.rstrip("\n") == "### Headers":
            header_line_index = i
            break
    if header_line_index is None:
        raise RuntimeError("missing '### Headers' section in landing page")

    start = header_line_index + 1
    end = start
    while end < len(lines) and not (lines[end].startswith("### ") or lines[end].startswith("## ")):
        end += 1

    new_block = [f"- ``{MODULE_NAME}/{container}``\n" for container in containers]
    updated = lines[:start] + new_block + lines[end:]

    new_text = "".join(updated)
    old_text = "".join(lines)
    if new_text != old_text:
        LANDING_PAGE.write_text(new_text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--headers-only",
        action="store_true",
        help="Parse only .h files when generating the WKAPI symbol graph (skip .m/.mm).",
    )
    parser.add_argument(
        "--no-swift",
        action="store_true",
        help="Skip Swift files when generating the WKAPI symbol graph.",
    )
    parser.add_argument(
        "--overwrite-type-pages",
        action="store_true",
        help="Overwrite existing generated type pages (manual pages like WKPreferencesPrivate.h.md should not use this).",
    )
    args = parser.parse_args()

    graph_cmd = [
        sys.executable,
        str(REPO_ROOT / "Scripts" / "generate_webkit_uiprocess_objc_symbol_graph.py"),
        "--write-index",
    ]
    if not args.headers_only:
        graph_cmd.append("--include-implementations")
    if not args.no_swift:
        graph_cmd.append("--include-swift")
    _run(graph_cmd)

    type_pages_cmd = [
        sys.executable,
        str(REPO_ROOT / "Scripts" / "generate_type_pages_from_symbol_index.py"),
        "--all-private-headers",
    ]
    if args.overwrite_type_pages:
        type_pages_cmd.append("--overwrite")
    _run(type_pages_cmd)

    _run([sys.executable, str(REPO_ROOT / "Scripts" / "update_module_landing_topics.py")])
    _run([sys.executable, str(REPO_ROOT / "Scripts" / "update_webkit_github_links.py")])
    _run([sys.executable, str(REPO_ROOT / "Scripts" / "ensure_entry_metadata.py")])
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
