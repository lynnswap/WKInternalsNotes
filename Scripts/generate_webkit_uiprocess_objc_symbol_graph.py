#!/usr/bin/env python3
"""
Generate a synthetic symbol graph for WKInternalsNotes from WebKit UIProcess Objective-C/Swift sources.

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
.m/.mm files (only @interface blocks, limited to WK*/_WK* types). Use --include-swift to
scan .swift files for non-public type declarations.
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

SWIFT_TYPE_KIND_MAP = {
    "class": ("swift.class", "Class", "class"),
    "struct": ("swift.struct", "Structure", "struct"),
    "enum": ("swift.enum", "Enumeration", "enum"),
    "protocol": ("swift.protocol", "Protocol", "protocol"),
    "actor": ("swift.actor", "Actor", "actor"),
}


@dataclass(frozen=True)
class SwiftTypeDecl:
    name: str
    kind: str


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


def _strip_swift_comments(text: str) -> str:
    # Best-effort removal for parsing; ignores string literal edge cases.
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"//.*", "", text)
    return text


_SWIFT_TYPE_DECL_RE = re.compile(
    r"^\s*(?:@[^\s]+\s+)*"
    r"(?:(public|open|internal|fileprivate|private)\s+)?"
    r"(?:(?:final|indirect|nonisolated|isolated|dynamic|lazy|required|convenience|override)\s+)*"
    r"(class|struct|enum|protocol|actor)\s+"
    r"([A-Za-z_][A-Za-z0-9_]*)"
)

_SWIFT_EXTENSION_RE = re.compile(r"^\s*extension\s+([A-Za-z_][A-Za-z0-9_\.]*)\b")
_SWIFT_ACCESS_LEVELS = {"public", "open", "internal", "fileprivate", "private"}
_SWIFT_MEMBER_KINDS = {"func", "init", "var", "let"}


@dataclass(frozen=True)
class SwiftExtensionMember:
    container: str
    kind: str  # func|init|var|let
    name: str
    path_component: str
    params: list[tuple[str, str, objc.SwiftType]]  # (external, internal, type)
    return_type: objc.SwiftType | None
    is_static: bool


def _strip_swift_attributes(text: str) -> str:
    return re.sub(r"^(?:@[A-Za-z_][A-Za-z0-9_]*(?:\([^)]*\))?\s+)+", "", text).strip()


def _split_swift_signature(text: str) -> str:
    depth = 0
    in_string = False
    escape = False
    for i, ch in enumerate(text):
        if in_string:
            if escape:
                escape = False
                continue
            if ch == "\\":
                escape = True
                continue
            if ch == "\"":
                in_string = False
            continue
        if ch == "\"":
            in_string = True
            continue
        if depth == 0 and ch in "{=":
            return text[:i].strip()
        if ch in "([{":
            depth += 1
            continue
        if ch in ")]}":
            depth = max(0, depth - 1)
            continue
    return text.strip()


def _extract_paren_content(text: str, start_index: int) -> tuple[str, int] | None:
    depth = 0
    start = None
    for i in range(start_index, len(text)):
        ch = text[i]
        if ch == "(":
            if depth == 0:
                start = i + 1
            depth += 1
            continue
        if ch == ")":
            depth -= 1
            if depth == 0 and start is not None:
                return text[start:i], i + 1
    return None


def _parse_swift_params(params_text: str) -> list[tuple[str, str, objc.SwiftType]]:
    params: list[tuple[str, str, objc.SwiftType]] = []
    for raw in objc._split_top_level_commas(params_text):  # noqa: SLF001
        part = raw.strip()
        if not part:
            continue
        part = part.split("=", 1)[0].strip()
        if ":" not in part:
            continue
        name_part, type_part = part.split(":", 1)
        name_part = name_part.strip()
        type_part = type_part.strip()
        type_part = re.sub(r"^(?:@[A-Za-z_][A-Za-z0-9_\.]*(?:\([^)]*\))?\s+)+", "", type_part)
        for prefix in ("inout ", "consuming ", "borrowing ", "isolated "):
            if type_part.startswith(prefix):
                type_part = type_part[len(prefix) :].strip()
        tokens = [t for t in name_part.split() if t and t not in {"inout", "consuming", "borrowing", "isolated"}]
        if not tokens:
            continue
        if len(tokens) == 1:
            external = internal = tokens[0]
        else:
            external = tokens[0]
            internal = tokens[1]
        params.append((external, internal, objc.SwiftType(type_part)))
    return params


def _swift_path_component(name: str, params: list[tuple[str, str, objc.SwiftType]]) -> str:
    if not params:
        return f"{name}()"
    labels = [external for (external, _internal, _ty) in params]
    return f"{name}({''.join(f'{label}:' for label in labels)})"


def _parse_swift_member_decl(decl: str, *, extension_has_spi: bool) -> SwiftExtensionMember | None:
    decl = _strip_swift_attributes(decl)
    decl = _split_swift_signature(decl)
    m = re.search(r"\b(func|init|var|let)\b", decl)
    if not m:
        return None

    kind = m.group(1)
    prefix = decl[: m.start()].strip()
    suffix = decl[m.end() :].strip()

    access = None
    for token in prefix.split():
        if token in _SWIFT_ACCESS_LEVELS:
            access = token
            break

    if access in {"public", "open"} and not extension_has_spi:
        return None
    if access in {"private", "fileprivate"}:
        return None

    is_static = bool(re.search(r"\b(static|class)\b", prefix))

    if kind in {"var", "let"}:
        m_prop = re.match(r"([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.+)$", suffix)
        if not m_prop:
            return None
        name = m_prop.group(1)
        type_str = _split_swift_signature(m_prop.group(2))
        return SwiftExtensionMember(
            container="",
            kind=kind,
            name=name,
            path_component=name,
            params=[],
            return_type=objc.SwiftType(type_str),
            is_static=is_static,
        )

    if kind == "func":
        m_name = re.match(r"([A-Za-z_][A-Za-z0-9_]*)", suffix)
        if not m_name:
            return None
        name = m_name.group(1)
        paren = _extract_paren_content(suffix, m_name.end())
        if not paren:
            return None
        params_text, end_index = paren
        params = _parse_swift_params(params_text)
        remainder = suffix[end_index:].strip()
        return_type = None
        if "->" in remainder:
            return_str = remainder.split("->", 1)[1].strip()
            return_str = _split_swift_signature(return_str)
            return_type = objc.SwiftType(return_str)
        return SwiftExtensionMember(
            container="",
            kind=kind,
            name=name,
            path_component=_swift_path_component(name, params),
            params=params,
            return_type=return_type,
            is_static=is_static,
        )

    if kind == "init":
        name = "init"
        if suffix.startswith(("?", "!")):
            suffix = suffix[1:]
        paren = _extract_paren_content(suffix, 0)
        if not paren:
            return None
        params_text, _end_index = paren
        params = _parse_swift_params(params_text)
        return SwiftExtensionMember(
            container="",
            kind=kind,
            name=name,
            path_component=_swift_path_component(name, params),
            params=params,
            return_type=None,
            is_static=False,
        )

    return None


def _iter_swift_extension_members(text: str) -> Iterable[SwiftExtensionMember]:
    lines = text.splitlines()
    depth = 0
    pending_extension_attrs: list[str] = []
    pending_member_attrs: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if depth == 0 and stripped.startswith("@"):
            pending_extension_attrs.append(stripped)
            i += 1
            continue

        m_ext = _SWIFT_EXTENSION_RE.match(line) if depth == 0 else None
        if m_ext:
            container = m_ext.group(1)
            extension_has_spi = any(attr.startswith("@_spi") or attr.startswith("@_spiOnly") for attr in pending_extension_attrs)
            pending_extension_attrs = []

            i += 1
            depth += line.count("{") - line.count("}")
            while i < len(lines):
                line = lines[i]
                stripped = line.strip()
                if depth == 1 and stripped.startswith("@"):
                    pending_member_attrs.append(stripped)
                    i += 1
                    continue
                if depth == 1:
                    first_token = stripped.split(" ", 1)[0] if stripped else ""
                    if first_token in _SWIFT_MEMBER_KINDS or any(tok in stripped for tok in (" func ", " init", " var ", " let ")):
                        decl_lines = [stripped]
                        i += 1
                        paren_depth = stripped.count("(") - stripped.count(")")
                        while i < len(lines) and paren_depth > 0:
                            next_line = lines[i].strip()
                            decl_lines.append(next_line)
                            paren_depth += next_line.count("(") - next_line.count(")")
                            i += 1
                        decl_text = " ".join(decl_lines)
                        decl_text = " ".join(pending_member_attrs) + " " + decl_text if pending_member_attrs else decl_text
                        pending_member_attrs = []
                        member = _parse_swift_member_decl(decl_text, extension_has_spi=extension_has_spi)
                        if member:
                            yield SwiftExtensionMember(
                                container=container,
                                kind=member.kind,
                                name=member.name,
                                path_component=member.path_component,
                                params=member.params,
                                return_type=member.return_type,
                                is_static=member.is_static,
                            )
                        depth += sum(dl.count("{") - dl.count("}") for dl in decl_lines)
                        continue

                pending_member_attrs = []
                depth += line.count("{") - line.count("}")
                if depth == 0:
                    i += 1
                    break
                i += 1
            continue

        depth += line.count("{") - line.count("}")
        if depth < 0:
            depth = 0
        i += 1


def _make_swift_extension_property_symbol(
    container: str,
    member: SwiftExtensionMember,
) -> dict[str, Any]:
    kind_id = "swift.type.property" if member.is_static else "swift.property"
    kind_name = "Type Property" if member.is_static else "Instance Property"
    swift_type = member.return_type or objc.SwiftType("Any")  # noqa: SLF001
    decl = [
        objc._fragment("keyword", "static" if member.is_static else "var"),  # noqa: SLF001
    ]
    if member.is_static:
        decl.append(objc._fragment("text", " "))  # noqa: SLF001
        decl.append(objc._fragment("keyword", "var"))  # noqa: SLF001
    decl.extend(
        [
            objc._fragment("text", " "),  # noqa: SLF001
            objc._fragment("identifier", member.name),  # noqa: SLF001
            objc._fragment("text", ": "),  # noqa: SLF001
            objc._type_fragment(swift_type),  # noqa: SLF001
        ]
    )
    return {
        "accessLevel": "public",
        "kind": {"identifier": kind_id, "displayName": kind_name},
        "identifier": {"precise": objc._make_precise_id(container, member.path_component), "interfaceLanguage": "swift"},  # noqa: SLF001
        "pathComponents": [container, member.path_component],
        "names": {"title": member.path_component, "subHeading": decl},
        "declarationFragments": decl,
    }


def _make_swift_extension_method_symbol(
    container: str,
    member: SwiftExtensionMember,
) -> dict[str, Any]:
    sig = objc.MethodSig(  # noqa: SLF001
        kind="type" if member.is_static else "instance",
        base_name=member.name,
        path_component=member.path_component,
        return_type=member.return_type,
        params=member.params,
    )
    return objc._make_method_symbol(container, sig, availability=[])  # noqa: SLF001


def _iter_swift_type_decls(text: str) -> Iterable[SwiftTypeDecl]:
    depth = 0
    for line in text.splitlines():
        if depth == 0:
            m = _SWIFT_TYPE_DECL_RE.match(line)
            if m:
                access = m.group(1)
                kind = m.group(2)
                name = m.group(3)
                if access not in {"public", "open"}:
                    yield SwiftTypeDecl(name=name, kind=kind)
        depth += line.count("{") - line.count("}")
        if depth < 0:
            depth = 0


def _iter_swift_files(ui_process_root: Path) -> Iterable[Path]:
    yield from _iter_files(ui_process_root, exts=(".swift",))


def _make_swift_container_symbol(type_name: str, *, kind: str) -> dict[str, Any]:
    kind_id, display_name, keyword = SWIFT_TYPE_KIND_MAP.get(kind, SWIFT_TYPE_KIND_MAP["class"])
    return {
        "accessLevel": "public",
        "kind": {"identifier": kind_id, "displayName": display_name},
        "identifier": {"precise": objc._make_precise_id(type_name), "interfaceLanguage": "swift"},  # noqa: SLF001
        "pathComponents": [type_name],
        "names": {
            "title": type_name,
            "navigator": [objc._fragment("identifier", type_name)],  # noqa: SLF001
            "subHeading": [
                objc._fragment("keyword", keyword),  # noqa: SLF001
                objc._fragment("text", " "),  # noqa: SLF001
                objc._fragment("identifier", type_name),  # noqa: SLF001
            ],
        },
        "declarationFragments": [
            objc._fragment("keyword", keyword),  # noqa: SLF001
            objc._fragment("text", " "),  # noqa: SLF001
            objc._fragment("identifier", type_name),  # noqa: SLF001
        ],
    }


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
    in_macro = False
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()

        if in_macro:
            if not line.rstrip().endswith("\\"):
                in_macro = False
            i += 1
            continue

        if stripped.startswith("#define"):
            if line.rstrip().endswith("\\"):
                in_macro = True
            i += 1
            continue

        if not stripped.startswith(starters):
            i += 1
            continue

        # C++ linkage specifications like `extern "C" {` are not declarations.
        # If we treat them as `extern` and scan until the next `;`, we can accidentally
        # consume an `@class Foo;` forward-decl and emit a bogus global variable symbol.
        if stripped.startswith("extern") and re.match(r'^extern\s+"[^"]+"\s*\{?\s*$', stripped):
            i += 1
            continue

        buf: list[str] = [line.rstrip()]
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
    include_swift: bool,
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

    if include_swift:
        for path in _iter_swift_files(ui_process_root):
            text = _strip_swift_comments(path.read_text(encoding="utf-8", errors="ignore"))
            for decl in _iter_swift_type_decls(text):
                if public.is_public_type(decl.name):
                    continue
                precise_id = objc._make_precise_id(decl.name)  # noqa: SLF001
                if precise_id in symbol_by_precise_id:
                    continue
                add_symbol(_make_swift_container_symbol(decl.name, kind=decl.kind))
                members_by_type_and_category.setdefault(decl.name, {})
            for member in _iter_swift_extension_members(text):
                container = member.container
                if "." in container:
                    continue
                if not _is_candidate_symbol_name(container):
                    continue
                container_id = objc._make_precise_id(container)  # noqa: SLF001
                if container_id not in symbol_by_precise_id:
                    add_symbol(objc._make_header_container_symbol(container))  # noqa: SLF001
                if member.kind in {"var", "let"}:
                    symbol = _make_swift_extension_property_symbol(container, member)
                else:
                    symbol = _make_swift_extension_method_symbol(container, member)
                add_symbol(symbol)
                add_relationship("memberOf", symbol["identifier"]["precise"], container_id)
                members_by_type_and_category.setdefault(container, {}).setdefault("Swift Extension", set()).add(
                    member.path_component
                )

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
    parser.add_argument(
        "--include-swift",
        action="store_true",
        help="Also scan .swift files for non-public type declarations.",
    )
    parser.add_argument("--write-index", action="store_true", help="Also write a JSON index next to the symbol graph.")
    args = parser.parse_args()

    public = _build_public_set(args.webkit_root)

    symbols, relationships, members_index = _collect_symbols_from_headers(
        args.webkit_root,
        public=public,
        include_implementations=args.include_implementations,
        include_swift=args.include_swift,
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
