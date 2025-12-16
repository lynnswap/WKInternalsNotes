#!/usr/bin/env python3
"""
Ensure entry pages contain a standard metadata section.

Entry pages are DocC documentation extensions rendered as symbol reference pages.
To keep pages machine-updatable and consistent, this script ensures:

  ## Metadata
  | Key | Value |
  | --- | ----- |
  | Status | Draft |
  | Last updated | YYYY-MM-DD |

as the last section of the page.

By default this only adds missing metadata; it does not overwrite existing values.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import generate_webkitspi_private_symbol_graph as gen


METADATA_HEADING = "## Metadata"
LAST_REVIEWED_PREFIX = "- Last reviewed:"
LAST_UPDATED_PREFIX = "- Last updated:"
DEFAULT_TABLE_HEADER = "| Key | Value |\n"
DEFAULT_TABLE_SEPARATOR = "| --- | ----- |\n"


def _splitlines_keepends(text: str) -> list[str]:
    return text.splitlines(keepends=True)


def _find_first_index(lines: list[str], predicate) -> int | None:
    for i, line in enumerate(lines):
        if predicate(line):
            return i
    return None


def _ensure_trailing_newline(text: str) -> str:
    if text.endswith("\n"):
        return text
    return text + "\n"


def _normalize_newlines(lines: list[str]) -> list[str]:
    return [line if line.endswith("\n") else line + "\n" for line in lines]


def _extract_metadata_section(lines: list[str]) -> tuple[list[str] | None, list[str]]:
    for i, line in enumerate(lines):
        if line.rstrip("\n") != METADATA_HEADING:
            continue

        start = i
        end = start + 1
        while end < len(lines):
            if lines[end].startswith("# "):
                break
            if lines[end].startswith("## ") and lines[end].rstrip("\n") != METADATA_HEADING:
                break
            end += 1

        return lines[start:end], lines[:start] + lines[end:]

    return None, lines


def _normalize_metadata_lines(lines: list[str]) -> list[str]:
    return [line.replace(LAST_REVIEWED_PREFIX, LAST_UPDATED_PREFIX) for line in lines]


def _strip_trailing_blank_lines(lines: list[str]) -> list[str]:
    trimmed = list(lines)
    while trimmed and trimmed[-1].strip() == "":
        trimmed.pop()
    return trimmed


def _build_default_metadata(*, status: str, updated: str) -> list[str]:
    return _build_metadata_table([("Status", status), ("Last updated", updated)])


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
            if key.lower() in {"key", "---"}:
                continue
            if set(key) == {"-"}:
                continue
            if key and value is not None:
                pairs.append((key, value))
            continue
    return pairs


def _build_metadata_table(pairs: list[tuple[str, str]]) -> list[str]:
    lines: list[str] = [f"{METADATA_HEADING}\n", DEFAULT_TABLE_HEADER, DEFAULT_TABLE_SEPARATOR]
    for key, value in pairs:
        lines.append(f"| {key} | {value} |\n")
    return lines


def _ensure_metadata(markdown: str, *, status: str, updated: str) -> str:
    lines = _normalize_newlines(_splitlines_keepends(_ensure_trailing_newline(markdown)))
    metadata_lines, rest_lines = _extract_metadata_section(lines)
    pairs: list[tuple[str, str]] = []
    if metadata_lines is not None:
        metadata_lines = _normalize_metadata_lines(_normalize_newlines(metadata_lines))
        body = [line for line in metadata_lines if line.rstrip("\n") != METADATA_HEADING]
        pairs = _parse_metadata_kv(body)

    existing: dict[str, str] = {}
    extra_pairs: list[tuple[str, str]] = []
    for key, value in pairs:
        normalized_key = "Last updated" if key == "Last reviewed" else key
        if normalized_key in {"Status", "Last updated"} and normalized_key not in existing and value:
            existing[normalized_key] = value
        else:
            extra_pairs.append((normalized_key, value))

    merged_pairs: list[tuple[str, str]] = [
        ("Status", existing.get("Status", status)),
        ("Last updated", existing.get("Last updated", updated)),
    ]
    merged_pairs.extend(extra_pairs)
    metadata_lines = _strip_trailing_blank_lines(_normalize_newlines(_build_metadata_table(merged_pairs)))

    rest_lines = _strip_trailing_blank_lines(rest_lines)

    if rest_lines:
        rest_lines.append("\n")

    updated_lines = rest_lines + metadata_lines
    return "".join(updated_lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--status", default="Draft", help="Initial status for new metadata blocks.")
    parser.add_argument(
        "--date",
        default=date.today().isoformat(),
        help="Date value for 'Last updated' (YYYY-MM-DD). Defaults to today.",
    )
    args = parser.parse_args()

    containers = gen.discover_header_containers()
    changed: list[Path] = []

    for _container, directory in containers.items():
        if not directory.exists():
            continue
        for md_path in sorted(directory.rglob("*.md")):
            original = md_path.read_text(encoding="utf-8")
            updated = _ensure_metadata(original, status=args.status, updated=args.date)
            if updated != original:
                md_path.write_text(updated, encoding="utf-8")
                changed.append(md_path)

    if changed:
        rels = [str(p.relative_to(gen.REPO_ROOT)) for p in changed]
        print("Updated:")
        for r in rels:
            print(f"  - {r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
