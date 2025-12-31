#!/usr/bin/env python3
"""
Update the module landing page Topics list from the synthetic symbol graph.

Reads:
  - Sources/WKInternalsNotes/Documentation.docc/SymbolGraphs/WKInternalsNotes.WKAPI.symbols.json

Rewrites:
  - Sources/WKInternalsNotes/Documentation.docc/WKInternalsNotes.md
    (the type lists under "## Topics")
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

TYPE_SECTION_ORDER: list[tuple[str, str]] = [
    ("Classes", "swift.class"),
    ("Structures", "swift.struct"),
    ("Enumerations", "swift.enum"),
    ("Protocols", "swift.protocol"),
    ("Actors", "swift.actor"),
]
TOPICS_HEADING = "## Topics"
LEGACY_SECTION_HEADING = "### Types"
LEGACY_SECTION_HEADING_CANDIDATES = [
    LEGACY_SECTION_HEADING,
    "### Cocoa (UIProcess/API/Cocoa)",  # legacy
]
NEW_TYPE_HEADINGS = [f"### {name}" for name, _ in TYPE_SECTION_ORDER]
LEGACY_TYPE_HEADINGS = [
    "#### Classes",
    "#### Structs",
    "#### Structures",
    "#### Enums",
    "#### Enumerations",
    "#### Protocols",
    "#### Actors",
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


def _rewrite_types_section(lines: list[str], sections: dict[str, list[str]]) -> list[str]:
    topics_index = None
    for i, line in enumerate(lines):
        if line.rstrip("\n") == TOPICS_HEADING:
            topics_index = i
            break
    if topics_index is None:
        raise RuntimeError(f"missing section heading: {TOPICS_HEADING}")

    topics_end = len(lines)
    for i in range(topics_index + 1, len(lines)):
        if lines[i].startswith("## "):
            topics_end = i
            break

    start = None
    mode = None
    for i in range(topics_index + 1, topics_end):
        candidate = lines[i].rstrip("\n")
        if candidate in LEGACY_SECTION_HEADING_CANDIDATES:
            start = i
            mode = "legacy"
            break
    if start is None:
        for i in range(topics_index + 1, topics_end):
            candidate = lines[i].rstrip("\n")
            if candidate in NEW_TYPE_HEADINGS:
                start = i
                mode = "flat"
                break
    if start is None:
        for i in range(topics_index + 1, topics_end):
            candidate = lines[i].rstrip("\n")
            if candidate in LEGACY_TYPE_HEADINGS:
                start = i
                mode = "legacy-subheadings"
                break

    if start is None or mode is None:
        raise RuntimeError("missing type headings under ## Topics")

    end = start + 1
    if mode == "flat":
        while end < topics_end:
            line = lines[end]
            if line.startswith("## "):
                break
            if line.startswith("### ") and line.rstrip("\n") not in NEW_TYPE_HEADINGS:
                break
            end += 1
    else:
        while end < topics_end:
            line = lines[end]
            if line.startswith("## ") or line.startswith("### "):
                break
            end += 1

    new_block: list[str] = []
    new_block.extend(lines[:start])
    if new_block and new_block[-1].strip() != "":
        new_block.append("\n")

    for section_name, _kind_id in TYPE_SECTION_ORDER:
        items = sections.get(section_name, [])
        if not items:
            continue
        new_block.append(f"### {section_name}\n")
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
    updated_lines = _rewrite_types_section(original_lines, sections=sections)
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
