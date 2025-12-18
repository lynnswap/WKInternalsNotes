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

SECTION_HEADING = "### Cocoa (UIProcess/API/Cocoa)"


def _extract_symbol_ref(markdown: str) -> str | None:
    for line in markdown.splitlines():
        if not line.startswith("# "):
            continue
        m = re.fullmatch(r"#\s+``([^`]+)``\s*", line)
        return m.group(1) if m else None
    return None


def _rewrite_bullets(lines: list[str], *, heading: str, new_bullets: list[str]) -> list[str]:
    heading_index = None
    for i, line in enumerate(lines):
        if line.rstrip("\n") == heading:
            heading_index = i
            break
    if heading_index is None:
        raise RuntimeError(f"missing section heading: {heading}")

    start = heading_index + 1
    end = start
    while end < len(lines):
        if lines[end].startswith("### ") or lines[end].startswith("## "):
            break
        end += 1

    bullet_block = [b if b.endswith("\n") else b + "\n" for b in new_bullets]
    return lines[:start] + bullet_block + lines[end:]


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
    updated_lines = _rewrite_bullets(original_lines, heading=SECTION_HEADING, new_bullets=bullets)
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

