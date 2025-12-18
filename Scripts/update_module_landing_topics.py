#!/usr/bin/env python3
"""
Update the module landing page Topics list from existing type pages.

Reads:
  - Sources/WKInternalsNotes/Documentation.docc/UIProcess/API/Cocoa/*.h.md

Rewrites:
  - Sources/WKInternalsNotes/Documentation.docc/WKInternalsNotes.md
    (the bullet list under "### Cocoa (UIProcess/API/Cocoa)")
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCC_ROOT = REPO_ROOT / "Sources" / "WKInternalsNotes" / "Documentation.docc"
LANDING_PAGE = DOCC_ROOT / "WKInternalsNotes.md"
COCOA_DIR = DOCC_ROOT / "UIProcess" / "API" / "Cocoa"

PREFERRED_SECTION_HEADING = "### Types"
SECTION_HEADING_CANDIDATES = [
    PREFERRED_SECTION_HEADING,
    "### Cocoa (UIProcess/API/Cocoa)",  # legacy
]


def _extract_symbol_ref(markdown: str) -> str | None:
    for line in markdown.splitlines():
        if not line.startswith("# "):
            continue
        m = re.fullmatch(r"#\s+``([^`]+)``\s*", line)
        return m.group(1) if m else None
    return None


def _rewrite_bullets(lines: list[str], *, heading: str, new_bullets: list[str]) -> list[str]:
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

    bullet_block = [b if b.endswith("\n") else b + "\n" for b in new_bullets]

    bullet_start = None
    for i in range(start, end):
        if lines[i].startswith("- "):
            bullet_start = i
            break
    if bullet_start is None:
        bullet_start = end

    # Keep any descriptive preamble between the heading and the bullet list.
    prefix = list(lines[:bullet_start])
    if prefix and prefix[-1].strip() != "" and bullet_block:
        prefix.append("\n")
    return prefix + bullet_block + list(lines[end:])


def main() -> int:
    if not LANDING_PAGE.exists():
        print(f"error: missing landing page: {LANDING_PAGE}", file=sys.stderr)
        return 2
    if not COCOA_DIR.exists():
        print(f"error: missing Cocoa dir: {COCOA_DIR}", file=sys.stderr)
        return 2

    symbol_refs: list[str] = []
    for path in sorted(COCOA_DIR.glob("*.h.md")):
        symbol_ref = _extract_symbol_ref(path.read_text(encoding="utf-8"))
        if symbol_ref:
            symbol_refs.append(symbol_ref)

    if not symbol_refs:
        print("error: no type pages found to extract symbols", file=sys.stderr)
        return 2

    symbol_refs = sorted(set(symbol_refs), key=str.casefold)
    bullets = [f"- ``{ref}``" for ref in symbol_refs]

    original_lines = LANDING_PAGE.read_text(encoding="utf-8").splitlines(keepends=True)
    updated_lines = _rewrite_bullets(original_lines, heading=PREFERRED_SECTION_HEADING, new_bullets=bullets)
    updated_text = "".join(updated_lines)
    original_text = "".join(original_lines)

    if updated_text != original_text:
        LANDING_PAGE.write_text(updated_text, encoding="utf-8")
        print(f"Updated: {LANDING_PAGE.relative_to(REPO_ROOT)} ({len(bullets)} bullets)")
    else:
        print(f"Unchanged: {LANDING_PAGE.relative_to(REPO_ROOT)} ({len(bullets)} bullets)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
