#!/usr/bin/env python3
"""
Generate DocC type pages from the synthetic symbol index.

This script reads:
  - Sources/WKInternalsNotes/Documentation.docc/SymbolGraphs/WKInternalsNotes.WKAPI.symbols.index.json
  - Sources/WKInternalsNotes/Documentation.docc/SymbolGraphs/WKInternalsNotes.WKAPI.symbols.header-index.json

and generates documentation extension pages (type pages) that group members by header:
  - Sources/WKInternalsNotes/Documentation.docc/UIProcess/API/Cocoa/<HeaderName>.h.md
  - Sources/WKInternalsNotes/Documentation.docc/UIProcess/API/Cocoa/<Symbol>.md

The output is intentionally minimal: Topics grouped by category, and a metadata table.

Type overviews (abstract) are intentionally omitted by default. Add them manually only when WebKit's
official headers contain an appropriate description (then translate it into Japanese). Otherwise,
keeping the overview blank is preferred over writing placeholders.
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

REVISION_FILE = REPO_ROOT / "WebKit.revision"
DOCC_ROOT = REPO_ROOT / "Sources" / "WKInternalsNotes" / "Documentation.docc"
INDEX_PATH = DOCC_ROOT / "SymbolGraphs" / "WKInternalsNotes.WKAPI.symbols.index.json"
HEADER_INDEX_PATH = DOCC_ROOT / "SymbolGraphs" / "WKInternalsNotes.WKAPI.symbols.header-index.json"
OUTPUT_DIR = DOCC_ROOT / "UIProcess" / "API" / "Cocoa"

DEFAULT_WEBKIT_CHECKOUT = REPO_ROOT / "References" / "WebKit"
WEBKIT_COCOA_HEADERS_DIR_REL = Path("Source/WebKit/UIProcess/API/Cocoa")
WEBKIT_HEADER_REPO_REL_DIR = "Source/WebKit/UIProcess/API/Cocoa"

MODULE_NAME = "WKInternalsNotes"


def _read_revision() -> str:
    for line in REVISION_FILE.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        return s
    raise RuntimeError(f"no revision found in: {REVISION_FILE}")


def _webkit_root_from_env() -> Path:
    env = os.environ.get("WKINTERNALS_WEBKIT_CHECKOUT")
    if env:
        return Path(env).expanduser()
    return DEFAULT_WEBKIT_CHECKOUT


def _find_header_for_symbol(symbol: str, *, webkit_headers_dir: Path) -> str | None:
    candidates = [f"{symbol}Private.h", f"{symbol}.h"]
    for name in candidates:
        if (webkit_headers_dir / name).exists():
            return name
    return None


def _header_sort_key(name: str) -> tuple[int, str]:
    lower = name.casefold()
    if "internal" in lower:
        return (2, lower)
    if "private" in lower:
        return (1, lower)
    return (0, lower)


def _format_symbol_link(container: str, member: str) -> str:
    return f"- ``{MODULE_NAME}/{container}/{member}``"

def _append_topic_group(
    lines: list[str],
    *,
    title: str,
    container: str,
    members: list[str],
) -> None:
    if not members:
        return
    lines.append(f"### {title}")
    lines.append("")
    lines.extend(_format_symbol_link(container, m) for m in members)
    lines.append("")


def _render_topics(
    container: str,
    categories: dict[str, list[str]],
    *,
    header_index: dict[str, dict[str, str]],
) -> list[str]:
    lines: list[str] = []
    lines.append("## Topics")
    lines.append("")

    all_members = {member for members in categories.values() for member in members}
    members_by_header: dict[str, dict[str, list[str]]] = {}
    unresolved = {"properties": [], "methods": []}
    member_headers = header_index.get(container, {})

    for member in sorted(all_members, key=str.casefold):
        header_name = member_headers.get(member)
        target = unresolved if header_name is None else members_by_header.setdefault(
            header_name,
            {"properties": [], "methods": []},
        )
        bucket = "methods" if "(" in member else "properties"
        target[bucket].append(member)

    properties_headers = [
        header_name for header_name, groups in members_by_header.items() if groups["properties"]
    ]
    methods_headers = [header_name for header_name, groups in members_by_header.items() if groups["methods"]]
    show_properties_from = len(properties_headers) > 1 or bool(unresolved["properties"])
    show_methods_from = len(methods_headers) > 1 or bool(unresolved["methods"])

    for header_name in sorted(members_by_header.keys(), key=_header_sort_key):
        groups = members_by_header[header_name]
        groups["properties"].sort(key=str.casefold)
        groups["methods"].sort(key=str.casefold)
        properties_title = (
            f"Properties (from {header_name})" if show_properties_from else "Properties"
        )
        methods_title = f"Methods (from {header_name})" if show_methods_from else "Methods"
        _append_topic_group(
            lines,
            title=properties_title,
            container=container,
            members=groups["properties"],
        )
        _append_topic_group(
            lines,
            title=methods_title,
            container=container,
            members=groups["methods"],
        )

    unresolved["properties"].sort(key=str.casefold)
    unresolved["methods"].sort(key=str.casefold)
    _append_topic_group(
        lines,
        title="Properties",
        container=container,
        members=unresolved["properties"],
    )
    _append_topic_group(
        lines,
        title="Methods",
        container=container,
        members=unresolved["methods"],
    )

    # Drop trailing blank line if present.
    while lines and lines[-1] == "":
        lines.pop()
    lines.append("")
    return lines


def _render_metadata(*, revision: str, header_name: str | None, today: str) -> list[str]:
    lines: list[str] = [
        "## Metadata",
        "| Key | Value |",
        "| --- | ----- |",
        "| Status | Draft |",
        f"| Last updated | {today} |",
        f"| WebKit revision | [`{revision}`](https://github.com/WebKit/WebKit/tree/{revision}) |",
    ]
    if header_name is not None:
        repo_rel = f"{WEBKIT_HEADER_REPO_REL_DIR}/{header_name}"
        lines.append(
            "| Header (WebKit repo-relative path) | "
            f"[`{header_name}`](https://github.com/WebKit/WebKit/blob/{revision}/{repo_rel}) |"
        )
    return lines + [""]


def _render_page(
    *,
    symbol: str,
    categories: dict[str, list[str]],
    revision: str,
    header_name: str | None,
    header_index: dict[str, dict[str, str]],
) -> str:
    today = date.today().isoformat()
    out: list[str] = []
    out.append(f"# ``{MODULE_NAME}/{symbol}``")
    out.append("")
    out.extend(_render_topics(symbol, categories, header_index=header_index))
    out.extend(_render_metadata(revision=revision, header_name=header_name, today=today))
    return "\n".join(out)


def _symbols_from_private_headers(*, webkit_headers_dir: Path, index: dict[str, dict[str, list[str]]]) -> list[str]:
    symbols: list[str] = []
    for header_path in sorted(webkit_headers_dir.glob("*Private.h")):
        stem = header_path.stem  # e.g. WKWebViewPrivate, _WKInspectorPrivate
        candidates: list[str] = []
        if stem.endswith("Private"):
            candidates.append(stem[: -len("Private")])
        candidates.append(stem)
        for cand in candidates:
            if cand in index:
                symbols.append(cand)
                break
    return sorted(set(symbols), key=str.casefold)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "symbols",
        nargs="*",
        help="Container symbol names to generate (e.g. WKWebView). Omit when using --all-private-headers.",
    )
    parser.add_argument(
        "--all-private-headers",
        action="store_true",
        help="Generate type pages for all *Private.h headers under WebKit UIProcess/API/Cocoa (if present in index).",
    )
    parser.add_argument(
        "--all-symbols",
        action="store_true",
        help="Generate type pages for all container symbols present in the index.",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files.")
    parser.add_argument(
        "--webkit-root",
        type=Path,
        default=_webkit_root_from_env(),
        help="Path to WebKit checkout (defaults to References/WebKit or WKINTERNALS_WEBKIT_CHECKOUT).",
    )
    args = parser.parse_args()

    revision = _read_revision()
    index: dict[str, dict[str, list[str]]] = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    header_index: dict[str, dict[str, str]] = {}
    if HEADER_INDEX_PATH.exists():
        header_index = json.loads(HEADER_INDEX_PATH.read_text(encoding="utf-8"))
    else:
        print(f"warning: missing header index: {HEADER_INDEX_PATH.relative_to(REPO_ROOT)}")

    webkit_headers_dir = args.webkit_root / WEBKIT_COCOA_HEADERS_DIR_REL
    if not webkit_headers_dir.exists():
        raise RuntimeError(f"missing WebKit Cocoa headers dir: {webkit_headers_dir}")

    if args.all_private_headers and args.all_symbols:
        raise RuntimeError("cannot combine --all-private-headers with --all-symbols")

    symbols = list(args.symbols)
    if args.all_private_headers:
        symbols = _symbols_from_private_headers(webkit_headers_dir=webkit_headers_dir, index=index)
    if args.all_symbols:
        symbols = sorted(index.keys(), key=str.casefold)

    if not symbols:
        raise RuntimeError("no symbols specified (pass symbols or --all-private-headers/--all-symbols)")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    written = 0
    skipped = 0

    for symbol in symbols:
        categories = index.get(symbol)
        if categories is None:
            print(f"warning: missing from index: {symbol}")
            skipped += 1
            continue

        header_name = _find_header_for_symbol(symbol, webkit_headers_dir=webkit_headers_dir)
        output_name = f"{Path(header_name).stem}.h.md" if header_name is not None else f"{symbol}.md"
        out_path = OUTPUT_DIR / output_name

        if out_path.exists() and not args.overwrite:
            print(f"skip: {out_path.relative_to(REPO_ROOT)} (already exists)")
            skipped += 1
            continue

        out_path.write_text(
            _render_page(
                symbol=symbol,
                categories=categories,
                revision=revision,
                header_name=header_name,
                header_index=header_index,
            ),
            encoding="utf-8",
        )
        print(f"wrote: {out_path.relative_to(REPO_ROOT)}")
        written += 1

    print(f"done: wrote {written}, skipped {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
