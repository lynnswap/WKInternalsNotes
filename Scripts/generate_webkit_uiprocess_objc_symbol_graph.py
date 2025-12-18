#!/usr/bin/env python3
"""
Generate a synthetic symbol graph for WKInternalsNotes from WebKit UIProcess Objective-C sources.

Goals:
  - Type-centric navigation (DocC-style):
      - Members declared in @interface <Type> (<Category>) are modeled as members of <Type>.
      - Type pages can group members by <Category> in Topics.
  - Expose top-level symbols at module root:
      - Top-level symbols (@protocol / typedef / NS_ENUM / NS_OPTIONS / extern) are modeled as
        module-level symbols so DocC can auto-group them (Protocols / Enumerations / Type Aliases / ...).
  - Filter out public API up-front (Rule A):
      - Build a public symbol set from "public headers" under UIProcess/API/Cocoa, then exclude
        matching symbols when generating the synthetic graph.

By default, this script parses only .h files. Use --include-implementations to also scan
.m/.mm files (only @interface blocks, limited to WK*/_WK* types).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import generate_webkitspi_private_symbol_graph as objc


REPO_ROOT = Path(__file__).resolve().parents[1]

DOCC_ROOT = REPO_ROOT / "Sources" / "WKInternalsNotes" / "Documentation.docc"
OUTPUT_DIR = DOCC_ROOT / "SymbolGraphs"
OUTPUT_PATH = OUTPUT_DIR / "WKInternalsNotes.WKAPI.symbols.json"

DEFAULT_WEBKIT_CHECKOUT = REPO_ROOT / "References" / "WebKit"
WEBKIT_UI_PROCESS_DIR = Path("Source/WebKit/UIProcess")
WEBKIT_PUBLIC_COCOA_DIR = Path("Source/WebKit/UIProcess/API/Cocoa")

EXCLUDED_PORT_PATH_PARTS = {
    "glib",
    "gtk",
    "wpe",
    "libwpe",
}


def _strip_comments(text: str) -> str:
    # Remove /* ... */ and // ... comments. This is a best-effort preprocessing for parsing.
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"//.*", "", text)
    return text


def _iter_files(root: Path, *, exts: tuple[str, ...]) -> Iterable[Path]:
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix not in exts:
            continue
        if EXCLUDED_PORT_PATH_PARTS.intersection(path.parts):
            continue
        yield path


@dataclass(frozen=True)
class InterfaceBlock:
    type_name: str
    category: str | None  # None: main interface, "": class extension (), "WKPrivate": category
    body_lines: list[str]


_INTERFACE_RE = re.compile(r"^\s*@interface\s+([A-Za-z_][A-Za-z0-9_]*)\b(.*)$")


def _parse_interface_header(rest: str) -> str | None:
    # Match "(Category)" right after the type name (whitespace allowed).
    # Examples:
    #   WKPreferences (WKPrivate)
    #   WKWebView ()
    m = re.match(r"\s*\(\s*([^)]*)\s*\)", rest)
    if not m:
        return None
    return m.group(1)


def _iter_interface_blocks(text: str) -> Iterable[InterfaceBlock]:
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = _INTERFACE_RE.match(line)
        if not m:
            i += 1
            continue

        type_name = m.group(1)
        rest = m.group(2)
        category = _parse_interface_header(rest)

        body: list[str] = []
        i += 1
        while i < len(lines):
            if re.match(r"^\s*@end\b", lines[i]):
                break
            body.append(lines[i])
            i += 1
        yield InterfaceBlock(type_name=type_name, category=category, body_lines=body)

        # Skip "@end"
        while i < len(lines) and not re.match(r"^\s*@end\b", lines[i]):
            i += 1
        if i < len(lines):
            i += 1


@dataclass(frozen=True)
class ProtocolBlock:
    name: str
    header_line: str
    body_lines: list[str]  # Empty for forward declarations.


_PROTOCOL_RE = re.compile(r"^\s*@protocol\b")


def _parse_protocol_names_from_forward_decl(line: str) -> list[str]:
    # Examples:
    #   @protocol Foo;
    #   @protocol Foo, Bar;
    #   @protocol Foo <Bar>;   (rare; best-effort)
    if not line.strip().endswith(";"):
        return []
    rest = line.split("@protocol", 1)[1]
    rest = rest.split(";", 1)[0]
    rest = rest.split("<", 1)[0]
    names = []
    for part in rest.split(","):
        name = part.strip()
        if name:
            names.append(name)
    return names


def _iter_protocol_blocks(text: str) -> Iterable[ProtocolBlock]:
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not _PROTOCOL_RE.match(line):
            i += 1
            continue

        # Forward declarations (no @end).
        forward_names = _parse_protocol_names_from_forward_decl(line)
        if forward_names:
            for name in forward_names:
                yield ProtocolBlock(name=name, header_line=line, body_lines=[])
            i += 1
            continue

        # Definitions (up to @end).
        try:
            name = objc._parse_protocol_symbol(line)  # noqa: SLF001
        except Exception:
            i += 1
            continue

        header_line = line
        body: list[str] = []
        i += 1
        while i < len(lines):
            if re.match(r"^\s*@end\b", lines[i]):
                break
            body.append(lines[i])
            i += 1
        yield ProtocolBlock(name=name, header_line=header_line, body_lines=body)

        # Skip "@end"
        while i < len(lines) and not re.match(r"^\s*@end\b", lines[i]):
            i += 1
        if i < len(lines):
            i += 1


def _iter_semicolon_decls(lines: list[str], *, starters: tuple[str, ...]) -> Iterable[str]:
    i = 0
    while i < len(lines):
        stripped = lines[i].lstrip()
        if not stripped.startswith(starters):
            i += 1
            continue

        buf: list[str] = [lines[i].rstrip()]
        i += 1
        while i < len(lines) and ";" not in buf[-1]:
            buf.append(lines[i].rstrip())
            if ";" in lines[i]:
                i += 1
                break
            i += 1
        yield "\n".join(buf).strip()


@dataclass(frozen=True)
class PublicSet:
    types: frozenset[str]
    member_keys: frozenset[str]  # "<Type>/<MemberPathComponent>"
    global_keys: frozenset[tuple[str, str]]  # (kind, name)

    def is_public_type(self, type_name: str) -> bool:
        return type_name in self.types

    def is_public_member(self, type_name: str, member_path: str) -> bool:
        return f"{type_name}/{member_path}" in self.member_keys

    def is_public_global(self, kind: str, name: str) -> bool:
        return (kind, name) in self.global_keys


def _is_candidate_symbol_name(name: str) -> bool:
    return name.startswith("WK") or name.startswith("_WK")


def _public_headers(webkit_root: Path) -> list[Path]:
    headers_dir = webkit_root / WEBKIT_PUBLIC_COCOA_DIR
    if not headers_dir.exists():
        raise RuntimeError(f"missing WebKit Cocoa headers dir: {headers_dir}")

    out: list[Path] = []
    for path in sorted(headers_dir.glob("*.h")):
        name = path.name
        if name.startswith("_"):
            continue
        if name.endswith(("Private.h", "Internal.h", "Testing.h")):
            continue
        out.append(path)
    return out


def _build_public_set(webkit_root: Path) -> PublicSet:
    types: set[str] = set()
    member_keys: set[str] = set()
    global_keys: set[tuple[str, str]] = set()

    for header in _public_headers(webkit_root):
        text = _strip_comments(header.read_text(encoding="utf-8", errors="ignore"))
        lines = text.splitlines()

        # Top-level symbols.
        for decl in _iter_semicolon_decls(lines, starters=("typedef", "extern", "FOUNDATION_EXPORT", "WK_EXTERN")):
            try:
                if "typedef NS_ENUM" in decl or "typedef NS_OPTIONS" in decl:
                    enum_name, _cases = objc._parse_enum_symbol(decl)  # noqa: SLF001
                    global_keys.add(("enum", enum_name))
                elif decl.lstrip().startswith("typedef"):
                    name, _ty = objc._parse_typedef_symbol(decl)  # noqa: SLF001
                    global_keys.add(("typealias", name))
                else:
                    name, _ty = objc._parse_extern_symbol(decl)  # noqa: SLF001
                    global_keys.add(("var", name))
            except Exception:
                continue

        for line in lines:
            m = re.match(r"^\s*@protocol\s+([A-Za-z_][A-Za-z0-9_]*)\b", line)
            if m:
                global_keys.add(("protocol", m.group(1)))

        # Protocol blocks: members.
        for block in _iter_protocol_blocks(text):
            if not _is_candidate_symbol_name(block.name):
                continue
            if not block.body_lines:
                continue
            for decl in _iter_semicolon_decls(block.body_lines, starters=("@property", "-", "+")):
                first = objc._condense_whitespace(decl.splitlines()[0])  # noqa: SLF001
                try:
                    if first.startswith("@property"):
                        name, _ty = objc._parse_property_symbol(decl)  # noqa: SLF001
                        member_keys.add(f"{block.name}/{name}")
                    elif first.startswith("-") or first.startswith("+"):
                        sig = objc._parse_method_symbol(decl)  # noqa: SLF001
                        member_keys.add(f"{block.name}/{sig.path_component}")
                except Exception:
                    continue

        # Interface blocks: types + members.
        for block in _iter_interface_blocks(text):
            if not _is_candidate_symbol_name(block.type_name):
                continue
            types.add(block.type_name)
            for decl in _iter_semicolon_decls(block.body_lines, starters=("@property", "-", "+")):
                first = objc._condense_whitespace(decl.splitlines()[0])  # noqa: SLF001
                try:
                    if first.startswith("@property"):
                        name, _ty = objc._parse_property_symbol(decl)  # noqa: SLF001
                        member_keys.add(f"{block.type_name}/{name}")
                    elif first.startswith("-") or first.startswith("+"):
                        sig = objc._parse_method_symbol(decl)  # noqa: SLF001
                        member_keys.add(f"{block.type_name}/{sig.path_component}")
                except Exception:
                    continue

    return PublicSet(types=frozenset(types), member_keys=frozenset(member_keys), global_keys=frozenset(global_keys))

def _make_top_level_protocol_symbol(name: str, *, availability: list[dict[str, Any]]) -> dict[str, Any]:
    decl = [
        objc._fragment("keyword", "protocol"),  # noqa: SLF001
        objc._fragment("text", " "),  # noqa: SLF001
        objc._fragment("identifier", name),  # noqa: SLF001
    ]
    symbol: dict[str, Any] = {
        "accessLevel": "public",
        "kind": {"identifier": "swift.protocol", "displayName": "Protocol"},
        "identifier": {"precise": objc._make_precise_id(name), "interfaceLanguage": "swift"},  # noqa: SLF001
        "pathComponents": [name],
        "names": {"title": name, "navigator": [objc._fragment("identifier", name)], "subHeading": decl},  # noqa: SLF001
        "declarationFragments": decl,
    }
    if availability:
        symbol["availability"] = availability
    return symbol


def _make_top_level_enum_symbol(enum_name: str, *, availability: list[dict[str, Any]]) -> dict[str, Any]:
    decl = [
        objc._fragment("keyword", "enum"),  # noqa: SLF001
        objc._fragment("text", " "),  # noqa: SLF001
        objc._fragment("identifier", enum_name),  # noqa: SLF001
    ]
    symbol: dict[str, Any] = {
        "accessLevel": "public",
        "kind": {"identifier": "swift.enum", "displayName": "Enumeration"},
        "identifier": {"precise": objc._make_precise_id(enum_name), "interfaceLanguage": "swift"},  # noqa: SLF001
        "pathComponents": [enum_name],
        "names": {
            "title": enum_name,
            "navigator": [objc._fragment("identifier", enum_name)],  # noqa: SLF001
            "subHeading": decl,
        },
        "declarationFragments": decl,
    }
    if availability:
        symbol["availability"] = availability
    return symbol


def _make_top_level_enum_case_symbol(
    enum_name: str,
    case_name: str,
    *,
    availability: list[dict[str, Any]],
) -> dict[str, Any]:
    decl = [
        objc._fragment("keyword", "case"),  # noqa: SLF001
        objc._fragment("text", " "),  # noqa: SLF001
        objc._fragment("identifier", case_name),  # noqa: SLF001
    ]
    symbol: dict[str, Any] = {
        "accessLevel": "public",
        "kind": {"identifier": "swift.enum.case", "displayName": "Case"},
        "identifier": {"precise": objc._make_precise_id(enum_name, case_name), "interfaceLanguage": "swift"},  # noqa: SLF001
        "pathComponents": [enum_name, case_name],
        "names": {"title": f"{enum_name}.{case_name}", "subHeading": decl},
        "declarationFragments": decl,
    }
    if availability:
        symbol["availability"] = availability
    return symbol


def _make_top_level_typealias_symbol(
    name: str,
    swift_type: objc.SwiftType,  # noqa: SLF001
    *,
    availability: list[dict[str, Any]],
) -> dict[str, Any]:
    decl = [
        objc._fragment("keyword", "typealias"),  # noqa: SLF001
        objc._fragment("text", " "),  # noqa: SLF001
        objc._fragment("identifier", name),  # noqa: SLF001
        objc._fragment("text", " = "),  # noqa: SLF001
        objc._type_fragment(swift_type),  # noqa: SLF001
    ]
    symbol: dict[str, Any] = {
        "accessLevel": "public",
        "kind": {"identifier": "swift.typealias", "displayName": "Type Alias"},
        "identifier": {"precise": objc._make_precise_id(name), "interfaceLanguage": "swift"},  # noqa: SLF001
        "pathComponents": [name],
        "names": {"title": name, "subHeading": decl},
        "declarationFragments": decl,
    }
    if availability:
        symbol["availability"] = availability
    return symbol


def _make_top_level_global_var_symbol(
    name: str,
    swift_type: objc.SwiftType,  # noqa: SLF001
    *,
    availability: list[dict[str, Any]],
) -> dict[str, Any]:
    decl = [
        objc._fragment("keyword", "let"),  # noqa: SLF001
        objc._fragment("text", " "),  # noqa: SLF001
        objc._fragment("identifier", name),  # noqa: SLF001
        objc._fragment("text", ": "),  # noqa: SLF001
        objc._type_fragment(swift_type),  # noqa: SLF001
    ]
    symbol: dict[str, Any] = {
        "accessLevel": "public",
        "kind": {"identifier": "swift.var", "displayName": "Global Variable"},
        "identifier": {"precise": objc._make_precise_id(name), "interfaceLanguage": "swift"},  # noqa: SLF001
        "pathComponents": [name],
        "names": {"title": name, "subHeading": decl},
        "declarationFragments": decl,
    }
    if availability:
        symbol["availability"] = availability
    return symbol


def _iter_global_decls(text: str) -> Iterable[str]:
    lines = text.splitlines()
    # NOTE: We intentionally ignore 'static' and macros here; only exported globals matter for docs.
    yield from _iter_semicolon_decls(lines, starters=("typedef", "extern", "FOUNDATION_EXPORT", "WK_EXTERN"))


def _collect_symbols_from_headers(
    webkit_root: Path,
    *,
    public: PublicSet,
    include_implementations: bool,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, dict[str, list[str]]]]:
    ui_process_root = webkit_root / WEBKIT_UI_PROCESS_DIR
    if not ui_process_root.exists():
        raise RuntimeError(f"missing WebKit UIProcess dir: {ui_process_root}")

    symbols: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    symbol_by_precise_id: dict[str, dict[str, Any]] = {}
    relationship_keys: set[tuple[str, str, str]] = set()

    members_by_type_and_category: dict[str, dict[str, set[str]]] = {}
    included_types: set[str] = set()

    def add_symbol(symbol: dict[str, Any]) -> None:
        precise = symbol["identifier"]["precise"]
        existing = symbol_by_precise_id.get(precise)
        if existing is not None:
            if "availability" not in existing and "availability" in symbol:
                existing["availability"] = symbol["availability"]
            return
        symbol_by_precise_id[precise] = symbol
        symbols.append(symbol)

    def add_relationship(kind: str, source: str, target: str) -> None:
        key = (kind, source, target)
        if key in relationship_keys:
            return
        relationship_keys.add(key)
        relationships.append({"kind": kind, "source": source, "target": target})

    exts = (".h", ".m", ".mm") if include_implementations else (".h",)

    for path in _iter_files(ui_process_root, exts=exts):
        text = _strip_comments(path.read_text(encoding="utf-8", errors="ignore"))
        if "@interface" not in text and "@protocol" not in text and "typedef" not in text and "extern" not in text:
            continue

        # Top-level declarations (globals).
        for decl in _iter_global_decls(text):
            decl_first = objc._condense_whitespace(decl.splitlines()[0])  # noqa: SLF001
            availability = objc._availability_from_objc_declaration(decl)  # noqa: SLF001

            try:
                if decl_first.startswith("@protocol"):
                    name = objc._parse_protocol_symbol(decl)  # noqa: SLF001
                    if not _is_candidate_symbol_name(name):
                        continue
                    if public.is_public_global("protocol", name):
                        continue
                    add_symbol(_make_top_level_protocol_symbol(name, availability=availability))
                elif "typedef NS_ENUM" in decl or "typedef NS_OPTIONS" in decl:
                    enum_name, cases = objc._parse_enum_symbol(decl)  # noqa: SLF001
                    if not _is_candidate_symbol_name(enum_name):
                        continue
                    if public.is_public_global("enum", enum_name):
                        continue
                    enum_symbol = _make_top_level_enum_symbol(enum_name, availability=availability)
                    add_symbol(enum_symbol)
                    enum_id = enum_symbol["identifier"]["precise"]
                    for case in cases:
                        case_symbol = _make_top_level_enum_case_symbol(enum_name, case, availability=availability)
                        add_symbol(case_symbol)
                        add_relationship("memberOf", case_symbol["identifier"]["precise"], enum_id)
                elif decl_first.startswith("typedef"):
                    name, swift_type = objc._parse_typedef_symbol(decl)  # noqa: SLF001
                    if not _is_candidate_symbol_name(name):
                        continue
                    if public.is_public_global("typealias", name):
                        continue
                    alias_type = swift_type if swift_type.name != "Any" else objc.SwiftType("Any")  # noqa: SLF001
                    add_symbol(_make_top_level_typealias_symbol(name, alias_type, availability=availability))
                elif re.match(r"^(extern|FOUNDATION_EXPORT|WK_EXTERN)\b", decl_first):
                    name, swift_type = objc._parse_extern_symbol(decl)  # noqa: SLF001
                    if not _is_candidate_symbol_name(name):
                        continue
                    if public.is_public_global("var", name):
                        continue
                    add_symbol(_make_top_level_global_var_symbol(name, swift_type, availability=availability))
            except Exception:
                continue

        # Protocol blocks (protocols + members).
        for block in _iter_protocol_blocks(text):
            if not _is_candidate_symbol_name(block.name):
                continue
            if public.is_public_global("protocol", block.name):
                continue

            availability = objc._availability_from_objc_declaration(block.header_line)  # noqa: SLF001
            add_symbol(_make_top_level_protocol_symbol(block.name, availability=availability))

            if not block.body_lines:
                continue

            protocol_id = objc._make_precise_id(block.name)  # noqa: SLF001
            for decl in _iter_semicolon_decls(block.body_lines, starters=("@property", "-", "+")):
                decl_first = objc._condense_whitespace(decl.splitlines()[0])  # noqa: SLF001
                availability = objc._availability_from_objc_declaration(decl)  # noqa: SLF001
                try:
                    if decl_first.startswith("@property"):
                        name, swift_type = objc._parse_property_symbol(decl)  # noqa: SLF001
                        if public.is_public_member(block.name, name):
                            continue
                        symbol = objc._make_property_symbol(block.name, name, swift_type, availability=availability)  # noqa: SLF001
                        add_symbol(symbol)
                        add_relationship("memberOf", symbol["identifier"]["precise"], protocol_id)
                        member_path = name
                    elif decl_first.startswith("-") or decl_first.startswith("+"):
                        sig = objc._parse_method_symbol(decl)  # noqa: SLF001
                        if public.is_public_member(block.name, sig.path_component):
                            continue
                        symbol = objc._make_method_symbol(block.name, sig, availability=availability)  # noqa: SLF001
                        add_symbol(symbol)
                        add_relationship("memberOf", symbol["identifier"]["precise"], protocol_id)
                        member_path = sig.path_component
                    else:
                        continue
                except Exception:
                    continue

                members_by_type_and_category.setdefault(block.name, {}).setdefault("Type", set()).add(member_path)

        # Interface blocks (types + members).
        for block in _iter_interface_blocks(text):
            if not _is_candidate_symbol_name(block.type_name):
                continue
            if include_implementations and path.suffix in {".m", ".mm"}:
                # Limit implementation scanning to categories / class extensions.
                if block.category is None:
                    continue

            for decl in _iter_semicolon_decls(block.body_lines, starters=("@property", "-", "+")):
                decl_first = objc._condense_whitespace(decl.splitlines()[0])  # noqa: SLF001
                availability = objc._availability_from_objc_declaration(decl)  # noqa: SLF001

                try:
                    if decl_first.startswith("@property"):
                        name, swift_type = objc._parse_property_symbol(decl)  # noqa: SLF001
                        if public.is_public_member(block.type_name, name):
                            continue
                        symbol = objc._make_property_symbol(block.type_name, name, swift_type, availability=availability)  # noqa: SLF001
                        add_symbol(symbol)
                        add_relationship(
                            "memberOf",
                            symbol["identifier"]["precise"],
                            objc._make_precise_id(block.type_name),  # noqa: SLF001
                        )
                        member_path = name
                    elif decl_first.startswith("-") or decl_first.startswith("+"):
                        sig = objc._parse_method_symbol(decl)  # noqa: SLF001
                        if public.is_public_member(block.type_name, sig.path_component):
                            continue
                        symbol = objc._make_method_symbol(block.type_name, sig, availability=availability)  # noqa: SLF001
                        add_symbol(symbol)
                        add_relationship(
                            "memberOf",
                            symbol["identifier"]["precise"],
                            objc._make_precise_id(block.type_name),  # noqa: SLF001
                        )
                        member_path = sig.path_component
                    else:
                        continue
                except Exception:
                    continue

                included_types.add(block.type_name)

                category = block.category
                if category == "":
                    category = "Class Extension"
                if category is None:
                    category = "Type"

                members_by_type_and_category.setdefault(block.type_name, {}).setdefault(category, set()).add(member_path)

    # Add container type symbols for any type that has at least one included member, and for any
    # non-public type definition we encountered in @interface blocks.
    for type_name in sorted(included_types):
        add_symbol(objc._make_header_container_symbol(type_name))  # noqa: SLF001

    # Deterministic order for Topics generation.
    members_index: dict[str, dict[str, list[str]]] = {}
    for type_name, categories in members_by_type_and_category.items():
        members_index[type_name] = {category: sorted(paths) for category, paths in categories.items()}

    return symbols, relationships, members_index


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--webkit-root",
        type=Path,
        default=Path(os.environ.get("WKINTERNALS_WEBKIT_CHECKOUT", DEFAULT_WEBKIT_CHECKOUT)),
        help="Path to WebKit checkout (defaults to References/WebKit or WKINTERNALS_WEBKIT_CHECKOUT).",
    )
    parser.add_argument(
        "--include-implementations",
        action="store_true",
        help="Also scan .m/.mm files (only @interface categories / class extensions for WK*/_WK* types).",
    )
    parser.add_argument("--write-index", action="store_true", help="Also write a JSON index next to the symbol graph.")
    args = parser.parse_args()

    public = _build_public_set(args.webkit_root)

    symbols, relationships, members_index = _collect_symbols_from_headers(
        args.webkit_root, public=public, include_implementations=args.include_implementations
    )

    platform = {
        "architecture": "arm64",
        "vendor": "apple",
        "operatingSystem": {"name": "macosx", "minimumVersion": {"major": 10, "minor": 13}},
    }

    graph = {
        "metadata": {
            "formatVersion": {"major": 0, "minor": 6, "patch": 0},
            "generator": "WKInternalsNotes UIProcess Objective-C synthetic symbol graph generator",
        },
        "module": {"name": objc.MODULE_NAME, "platform": platform},
        "symbols": symbols,
        "relationships": relationships,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(graph, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if args.write_index:
        index_path = OUTPUT_PATH.with_suffix(".index.json")
        index_path.write_text(json.dumps(members_index, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"Wrote: {OUTPUT_PATH.relative_to(REPO_ROOT)} ({len(symbols)} symbols, {len(relationships)} relationships)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
