#!/usr/bin/env python3
"""
Generate a DocC "Kind" playground symbol graph for DocCKindPlayground.

This script reads Swift-DocC's `DocumentationNode.Kind` definitions (Kind.swift)
from a local swift-docc checkout and generates a synthetic symbol graph that
contains one symbol per kind. This makes it easy to visually compare how DocC
renders different kinds (navigator icon, role heading, etc.).

Default swift-docc checkout path:
  ~/Dev/swift-docc (override with SWIFT_DOCC_ROOT)

Output (default):
  Sources/DocCKindPlayground/Documentation.docc/SymbolGraphs/DocCKindPlayground.Kinds.symbols.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCC_ROOT = REPO_ROOT / "Sources" / "DocCKindPlayground" / "Documentation.docc"
DEFAULT_OUTPUT_PATH = DOCC_ROOT / "SymbolGraphs" / "DocCKindPlayground.Kinds.symbols.json"

DEFAULT_SWIFT_DOCC_ROOT = Path(
    os.environ.get("SWIFT_DOCC_ROOT", str(Path.home() / "Dev" / "swift-docc"))
)
KIND_SWIFT_RELATIVE_PATH = Path("Sources/SwiftDocC/Model/Kind.swift")

DEFAULT_MODULE_NAME = "DocCKindPlayground"
PRECISE_ID_PREFIX = "wkapi-kindplayground"


@dataclass(frozen=True)
class DoccKind:
    case_name: str  # e.g. "namespace" (no leading dot)
    display_name: str  # e.g. "Namespace"
    kind_id: str  # e.g. "org.swift.docc.kind.namespace"
    is_symbol: bool
    is_page: bool


DOC_KIND_TO_SYMBOL_KIND_RAW: dict[str, str] = {
    # Containers
    "module": "module",
    "class": "class",
    "structure": "struct",
    "enumeration": "enum",
    "protocol": "protocol",
    "extension": "extension",
    "dictionary": "dictionary",
    "httpRequest": "httpRequest",
    "namespace": "namespace",
    # Leaves
    "localVariable": "var",
    "globalVariable": "var",
    "typeAlias": "typealias",
    "typeDef": "typealias",
    "typeConstant": "type.property",
    "associatedType": "associatedtype",
    "function": "func",
    "operator": "func.op",
    "macro": "macro",
    "union": "union",
    # Member-only leaves
    "dictionaryKey": "dictionaryKey",
    "enumerationCase": "enum.case",
    "httpBody": "httpBody",
    "httpParameter": "httpParameter",
    "httpResponse": "httpResponse",
    "initializer": "init",
    "deinitializer": "deinit",
    "instanceMethod": "method",
    "instanceProperty": "property",
    "instanceSubscript": "subscript",
    "instanceVariable": "ivar",
    "typeMethod": "type.method",
    "typeProperty": "type.property",
    "typeSubscript": "type.subscript",
    # Extended symbols
    "extendedModule": "extendedModule",
    "extendedStructure": "extendedStructure",
    "extendedClass": "extendedClass",
    "extendedEnumeration": "extendedEnumeration",
    "extendedProtocol": "extendedProtocol",
    "unknownExtendedType": "unknownExtendedType",
    # Other
    "object": "dictionary",
    # Not in allKnownValues but useful
    "snippet": "snippet",
}


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate DocC kind playground symbol graph.")
    parser.add_argument(
        "--module-name",
        default=DEFAULT_MODULE_NAME,
        help=f"Symbol graph module name (default: {DEFAULT_MODULE_NAME})",
    )
    parser.add_argument(
        "--swift-docc-root",
        type=Path,
        default=DEFAULT_SWIFT_DOCC_ROOT,
        help=(
            "Path to a swift-docc checkout "
            f"(default: {DEFAULT_SWIFT_DOCC_ROOT}; or set SWIFT_DOCC_ROOT)"
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help=f"Output .symbols.json path (default: {DEFAULT_OUTPUT_PATH.relative_to(REPO_ROOT)})",
    )
    parser.add_argument(
        "--include-snippet",
        action="store_true",
        help="Also include Kind.snippet (not in allKnownValues).",
    )
    return parser.parse_args(argv)


def _make_precise_id(module_name: str, *path_components: str) -> str:
    joined = "/".join(path_components)
    return f"{PRECISE_ID_PREFIX}:{module_name}/{joined}"


def _fragment(kind: str, spelling: str) -> dict[str, Any]:
    return {"kind": kind, "spelling": spelling}


def _parse_kind_swift(kind_swift_path: Path) -> tuple[list[DoccKind], set[str]]:
    text = kind_swift_path.read_text(encoding="utf-8")

    # Parse isPage == false cases from:
    # case .unknown, .volume, ...
    is_page_false: set[str] = set()
    m = re.search(r"public var isPage: Bool\s*\{\s*switch self \{(.*?)\}\s*\}", text, re.S)
    if m:
        block = m.group(1)
        case_m = re.search(r"case\s+(.*?)\s*:\s*\n\s*return false", block, re.S)
        if case_m:
            raw = re.sub(r"\s+", " ", case_m.group(1)).strip()
            items = [s.strip() for s in raw.split(",") if s.strip()]
            for item in items:
                if item.startswith("."):
                    is_page_false.add(item[1:])

    # Parse static kind definitions.
    kind_defs: dict[str, tuple[str, str, bool]] = {}
    pat = re.compile(
        r'public static let\s+([A-Za-z0-9_`]+)\s*=\s*DocumentationNode\.Kind\(name:\s*"([^"]+)",\s*id:\s*"([^"]+)",\s*isSymbol:\s*(true|false)\)'
    )
    for m in pat.finditer(text):
        raw_name = m.group(1)
        case_name = raw_name[1:-1] if raw_name.startswith("`") and raw_name.endswith("`") else raw_name
        kind_defs[case_name] = (m.group(2), m.group(3), m.group(4) == "true")

    # Parse allKnownValues list.
    all_known: list[str] = []
    m = re.search(r"allKnownValues:\s*\[DocumentationNode\.Kind\]\s*=\s*\[(.*?)\]\s*\n", text, re.S)
    if m:
        body = re.sub(r"//.*", "", m.group(1))
        body = body.replace("\n", " ")
        all_known = [s.strip() for s in body.split(",") if s.strip()]

    kinds: list[DoccKind] = []
    for item in all_known:
        if not item.startswith("."):
            continue
        key = item[1:]
        display_name, kind_id, is_symbol = kind_defs.get(key, (key, f"org.swift.docc.kind.{key}", False))
        kinds.append(
            DoccKind(
                case_name=key,
                display_name=display_name,
                kind_id=kind_id,
                is_symbol=is_symbol,
                is_page=key not in is_page_false,
            )
        )

    return kinds, is_page_false


def _symbol_kind_identifier(kind: DoccKind) -> str:
    raw = DOC_KIND_TO_SYMBOL_KIND_RAW.get(kind.case_name)
    if raw is None:
        # Use the DocC kind id as a "probe" for kinds that don't map to SymbolKit.
        return kind.kind_id
    return f"swift.{raw}"


def _declaration_for_case(case_name: str) -> list[dict[str, Any]]:
    keyword_map: dict[str, str] = {
        "class": "class",
        "structure": "struct",
        "enumeration": "enum",
        "protocol": "protocol",
        "extension": "extension",
        "namespace": "namespace",
        "module": "module",
        "dictionary": "dictionary",
        "object": "object",
        "function": "func",
        "operator": "operator",
        "macro": "macro",
        "union": "union",
        "globalVariable": "let",
        "localVariable": "let",
        "typeAlias": "typealias",
        "typeDef": "typealias",
        "associatedType": "associatedtype",
        "initializer": "init",
        "deinitializer": "deinit",
        "instanceMethod": "func",
        "typeMethod": "static func",
        "instanceProperty": "var",
        "typeProperty": "static var",
        "typeConstant": "static let",
        "instanceSubscript": "subscript",
        "typeSubscript": "static subscript",
        "instanceVariable": "var",
    }

    keyword = keyword_map.get(case_name, "kind")
    parts = []
    for i, token in enumerate(keyword.split()):
        if i > 0:
            parts.append(_fragment("text", " "))
        parts.append(_fragment("keyword", token))
    parts.append(_fragment("text", " "))
    parts.append(_fragment("identifier", case_name))
    if case_name in {"function", "instanceMethod", "typeMethod", "operator", "macro"}:
        parts.append(_fragment("text", "()"))
    return parts


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(list(argv) if argv is not None else sys.argv[1:])
    kind_swift_path = args.swift_docc_root / KIND_SWIFT_RELATIVE_PATH
    if not kind_swift_path.exists():
        print(f"error: missing Kind.swift: {kind_swift_path}", file=sys.stderr)
        return 2

    kinds, is_page_false = _parse_kind_swift(kind_swift_path)
    if args.include_snippet and "snippet" not in {k.case_name for k in kinds}:
        # Best-effort: Kind.snippet exists but is not in allKnownValues.
        kinds.append(
            DoccKind(
                case_name="snippet",
                display_name="Snippet",
                kind_id="org.swift.docc.kind.snippet",
                is_symbol=True,
                is_page=False,
            )
        )

    module_name: str = args.module_name

    platform = {
        "architecture": "arm64",
        "vendor": "apple",
        "operatingSystem": {"name": "macosx", "minimumVersion": {"major": 10, "minor": 13}},
    }

    symbols: list[dict[str, Any]] = []

    generated_count = 0
    for kind in kinds:
        symbol_name = kind.case_name
        symbol_precise = _make_precise_id(module_name, symbol_name)
        kind_identifier = _symbol_kind_identifier(kind)

        decl = _declaration_for_case(kind.case_name)
        title = symbol_name
        if kind.case_name in is_page_false:
            title = f"{symbol_name} (isPage=false)"

        symbols.append(
            {
                "accessLevel": "public",
                "kind": {"identifier": kind_identifier, "displayName": kind.display_name},
                "identifier": {"precise": symbol_precise, "interfaceLanguage": "swift"},
                "pathComponents": [symbol_name],
                "names": {"title": title, "navigator": [_fragment("identifier", title)], "subHeading": decl},
                "declarationFragments": decl,
            }
        )
        generated_count += 1

    graph = {
        "metadata": {
            "formatVersion": {"major": 0, "minor": 6, "patch": 0},
            "generator": "DocCKindPlayground DocC kind playground generator",
        },
        "module": {"name": module_name, "platform": platform},
        "symbols": symbols,
        "relationships": [],
    }

    output_path: Path = args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(graph, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    wrote = output_path
    if wrote.is_absolute() and REPO_ROOT in wrote.parents:
        wrote = wrote.relative_to(REPO_ROOT)

    symbol_kind_mapped = sum(1 for k in kinds if k.case_name in DOC_KIND_TO_SYMBOL_KIND_RAW)
    print(f"Wrote: {wrote} ({generated_count} kinds, {symbol_kind_mapped} SymbolKit-mapped)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
