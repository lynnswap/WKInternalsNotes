#!/usr/bin/env python3
"""
Update the module landing page Types list from the synthetic symbol graph.

Reads:
  - Sources/WKInternalsNotes/Documentation.docc/SymbolGraphs/WKInternalsNotes.WKAPI.symbols.json

Rewrites:
  - Sources/WKInternalsNotes/Documentation.docc/WKInternalsNotes.md
    (the bullet list under "### Cocoa (UIProcess/API/Cocoa)")
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCC_ROOT = REPO_ROOT / "Sources" / "WKInternalsNotes" / "Documentation.docc"
LANDING_PAGE = DOCC_ROOT / "WKInternalsNotes.md"
SYMBOL_GRAPH_PATH = DOCC_ROOT / "SymbolGraphs" / "WKInternalsNotes.WKAPI.symbols.json"
MODULE_NAME = "WKInternalsNotes"

PREFERRED_SECTION_HEADING = "### Types"
SECTION_HEADING_CANDIDATES = [
    PREFERRED_SECTION_HEADING,
    "### Cocoa (UIProcess/API/Cocoa)",  # legacy
]

TYPE_SECTION_ORDER: list[tuple[str, str]] = [
    ("Classes", "swift.class"),
    ("Structs", "swift.struct"),
    ("Enums", "swift.enum"),
    ("Protocols", "swift.protocol"),
    ("Actors", "swift.actor"),
]


def _collect_types() -> dict[str, list[str]]:
    data = json.loads(SYMBOL_GRAPH_PATH.read_text(encoding="utf-8"))
    symbols = data.get("symbols", [])

    sections: dict[str, set[str]] = {name: set() for name, _ in TYPE_SECTION_ORDER}
    for symbol in symbols:
        kind = symbol.get("kind", {}).get("identifier")
        name = None
        path_components = symbol.get("pathComponents") or []
        if len(path_components) != 1:
            continue
        name = path_components[0]
        for section_name, kind_id in TYPE_SECTION_ORDER:
            if kind == kind_id:
                sections[section_name].add(f"{MODULE_NAME}/{name}")
                break

    return {key: sorted(values, key=str.casefold) for key, values in sections.items()}


def _rewrite_types_section(lines: list[str], *, heading: str, sections: dict[str, list[str]]) -> list[str]:
    heading_index = None
    found_heading = None
    for i, line in enumerate(lines):
        candidate = line.rstrip("\n")
        if candidate in SECTION_HEADING_CANDIDATES:
            heading_index = i
            found_heading = candidate
            break
    if heading_index is None or found_heading is None:
        raise RuntimeError(f"missing section heading: {heading}")

    if found_heading != heading:
        lines = list(lines)
        lines[heading_index] = heading + ("\n" if lines[heading_index].endswith("\n") else "")

    start = heading_index + 1
    end = start
    while end < len(lines):
        if lines[end].startswith("### ") or lines[end].startswith("## "):
            break
        end += 1

    preamble: list[str] = []
    preamble_end = start
    while preamble_end < end:
        if lines[preamble_end].startswith("#### ") or lines[preamble_end].startswith("- "):
            break
        preamble.append(lines[preamble_end])
        preamble_end += 1

    new_block: list[str] = []
    new_block.extend(lines[:start])
    new_block.extend(preamble)
    if preamble and preamble[-1].strip() != "":
        new_block.append("\n")

    for section_name, _kind_id in TYPE_SECTION_ORDER:
        items = sections.get(section_name, [])
        if not items:
            continue
        new_block.append(f"#### {section_name}\n")
        for item in items:
            new_block.append(f"- ``{item}``\n")
        new_block.append("\n")

    while new_block and new_block[-1].strip() == "":
        new_block.pop()
    new_block.append("\n")

    return new_block + list(lines[end:])


def main() -> int:
    if not LANDING_PAGE.exists():
        print(f"error: missing landing page: {LANDING_PAGE}", file=sys.stderr)
        return 2
    if not SYMBOL_GRAPH_PATH.exists():
        print(f"error: missing symbol graph: {SYMBOL_GRAPH_PATH}", file=sys.stderr)
        return 2

    sections = _collect_types()
    if not any(sections.values()):
        print("error: no symbols found in symbol graph", file=sys.stderr)
        return 2

    original_lines = LANDING_PAGE.read_text(encoding="utf-8").splitlines(keepends=True)
    updated_lines = _rewrite_types_section(original_lines, heading=PREFERRED_SECTION_HEADING, sections=sections)
    updated_text = "".join(updated_lines)
    original_text = "".join(original_lines)

    if updated_text != original_text:
        LANDING_PAGE.write_text(updated_text, encoding="utf-8")
        count = sum(len(items) for items in sections.values())
        print(f"Updated: {LANDING_PAGE.relative_to(REPO_ROOT)} ({count} symbols)")
    else:
        count = sum(len(items) for items in sections.values())
        print(f"Unchanged: {LANDING_PAGE.relative_to(REPO_ROOT)} ({count} symbols)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
