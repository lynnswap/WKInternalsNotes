#!/usr/bin/env python3
"""
Replace `<doc:...>` links with symbol links for WKInternalsNotes entry pages.

After converting entry pages into documentation extensions, the old article-based
`<doc:...>` identifiers no longer resolve. This script updates header overview pages
to use symbol links instead.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCC_ROOT = REPO_ROOT / "Sources" / "WKInternalsNotes" / "Documentation.docc"
WEBKIT_SOURCE_WEBKIT_ROOT = DOCC_ROOT
COCOA_API_ROOT = WEBKIT_SOURCE_WEBKIT_ROOT / "UIProcess" / "API" / "Cocoa"


def _build_doc_id_to_symbol_ref() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for container_dir in sorted(COCOA_API_ROOT.iterdir()):
        if not container_dir.is_dir() or container_dir.name.startswith("."):
            continue
        for md_path in sorted(container_dir.rglob("*.md")):
            first_line = md_path.read_text(encoding="utf-8").splitlines()[0]
            m = re.match(r"^#\s+``([^`]+)``\s*$", first_line)
            if not m:
                continue
            mapping[md_path.stem] = m.group(1)
    return mapping


def _rewrite_doc_links(path: Path, mapping: dict[str, str]) -> tuple[str, list[str]]:
    original = path.read_text(encoding="utf-8")
    unresolved: list[str] = []

    def repl(match: re.Match[str]) -> str:
        doc_id = match.group(1)
        symbol_ref = mapping.get(doc_id)
        if symbol_ref is None:
            unresolved.append(doc_id)
            return match.group(0)
        return f"``{symbol_ref}``"

    updated = re.sub(r"<doc:([^>]+)>", repl, original)
    return updated, sorted(set(unresolved))


def main() -> int:
    mapping = _build_doc_id_to_symbol_ref()
    if not mapping:
        print("error: no symbol mappings found; run the conversion step first", file=sys.stderr)
        return 2

    targets = sorted(COCOA_API_ROOT.glob("*.h.md"))

    had_unresolved = False
    for path in targets:
        if not path.exists():
            continue
        updated, unresolved = _rewrite_doc_links(path, mapping)
        original = path.read_text(encoding="utf-8")
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"Updated: {path.relative_to(REPO_ROOT)}")
        if unresolved:
            had_unresolved = True
            print(f"warning: unresolved <doc:...> in {path.relative_to(REPO_ROOT)}:", file=sys.stderr)
            for doc_id in unresolved[:25]:
                print(f"  - {doc_id}", file=sys.stderr)
            if len(unresolved) > 25:
                print(f"  ... ({len(unresolved)} total)", file=sys.stderr)

    return 0 if not had_unresolved else 1


if __name__ == "__main__":
    raise SystemExit(main())
