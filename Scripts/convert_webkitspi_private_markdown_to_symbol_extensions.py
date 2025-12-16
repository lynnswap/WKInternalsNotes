#!/usr/bin/env python3
"""
Convert WKInternalsNotes private header markdown pages into DocC documentation extensions.

This updates the H1 title of each entry page to use a symbol link, e.g.:
  # ``WKInternalsNotes/WKPreferencesPrivate/_acceleratedDrawingEnabled``

so DocC renders the page as a symbol reference page (not an article).
"""

from __future__ import annotations

import sys
from pathlib import Path

import generate_webkitspi_private_symbol_graph as gen


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCC_ROOT = REPO_ROOT / "Sources" / "WKInternalsNotes" / "Documentation.docc"
WEBKIT_SOURCE_WEBKIT_ROOT = DOCC_ROOT
COCOA_API_ROOT = WEBKIT_SOURCE_WEBKIT_ROOT / "UIProcess" / "API" / "Cocoa"


def _replace_first_heading(markdown: str, new_heading_line: str) -> str:
    lines = markdown.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            lines[i] = new_heading_line
            return "\n".join(lines) + ("\n" if markdown.endswith("\n") else "")
    return markdown


def _rename_declaration_heading(markdown: str) -> str:
    # Avoid a duplicate "Declaration" section since the symbol page already has one.
    lines = markdown.splitlines()
    changed = False
    for i, line in enumerate(lines):
        if line.strip() == "## Declaration":
            lines[i] = "## Objective-C Declaration"
            changed = True
            break
    if not changed:
        return markdown
    return "\n".join(lines) + ("\n" if markdown.endswith("\n") else "")


def _symbol_ref_for_entry(container: str, markdown: str) -> str | None:
    objc_block = gen._extract_first_objc_code_block(markdown)  # noqa: SLF001
    if objc_block is None:
        return None

    first_line = gen._condense_whitespace(objc_block.splitlines()[0])  # noqa: SLF001

    if "typedef NS_ENUM" in objc_block or "typedef NS_OPTIONS" in objc_block:
        enum_name, _cases = gen._parse_enum_symbol(objc_block)  # noqa: SLF001
        return f"{gen.MODULE_NAME}/{container}/{enum_name}"

    if first_line.startswith("@property"):
        name, _ty = gen._parse_property_symbol(objc_block)  # noqa: SLF001
        return f"{gen.MODULE_NAME}/{container}/{name}"

    if first_line.startswith("-") or first_line.startswith("+"):
        sig = gen._parse_method_symbol(objc_block)  # noqa: SLF001
        return f"{gen.MODULE_NAME}/{container}/{sig.path_component}"

    if first_line.startswith("@protocol"):
        name = gen._parse_protocol_symbol(objc_block)  # noqa: SLF001
        return f"{gen.MODULE_NAME}/{container}/{name}"

    if first_line.startswith("@interface"):
        name = gen._parse_interface_symbol(objc_block)  # noqa: SLF001
        return f"{gen.MODULE_NAME}/{container}/{name}"

    if first_line.startswith("typedef"):
        name, _ty = gen._parse_typedef_symbol(objc_block)  # noqa: SLF001
        return f"{gen.MODULE_NAME}/{container}/{name}"

    if first_line.startswith("extern") or first_line.startswith("FOUNDATION_EXPORT") or first_line.startswith("WK_EXTERN"):
        name, _ty = gen._parse_extern_symbol(objc_block)  # noqa: SLF001
        return f"{gen.MODULE_NAME}/{container}/{name}"

    return None


def main() -> int:
    containers = gen.discover_header_containers()

    changed_files: list[Path] = []

    for container, directory in containers.items():
        if not directory.exists():
            continue
        for md_path in sorted(directory.rglob("*.md")):
            original = md_path.read_text(encoding="utf-8")
            symbol_ref = _symbol_ref_for_entry(container, original)
            if symbol_ref is None:
                continue

            updated = original
            updated = _replace_first_heading(updated, f"# ``{symbol_ref}``")
            updated = _rename_declaration_heading(updated)

            if updated != original:
                md_path.write_text(updated, encoding="utf-8")
                changed_files.append(md_path)

    for md_path in sorted(COCOA_API_ROOT.glob("*.h.md")):
        original = md_path.read_text(encoding="utf-8")
        if md_path.name.endswith(".h.md"):
            container = md_path.name[: -len(".h.md")]
        else:
            container = md_path.stem
        updated = _replace_first_heading(original, f"# ``{gen.MODULE_NAME}/{container}``")
        if updated != original:
            md_path.write_text(updated, encoding="utf-8")
            changed_files.append(md_path)

    if changed_files:
        rels = [str(p.relative_to(REPO_ROOT)) for p in changed_files]
        print("Updated:")
        for r in rels:
            print(f"  - {r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
