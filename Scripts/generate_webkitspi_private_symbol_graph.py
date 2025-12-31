#!/usr/bin/env python3
"""
Generate a synthetic symbol graph for WKInternalsNotes DocC entry pages.

NOTE: This is a legacy generator kept for the parsing helpers it provides.
The primary symbol graph used by DocC is now generated from WebKit sources via:
  - Scripts/generate_webkit_uiprocess_objc_symbol_graph.py

This script scans DocC markdown pages under:
  - Sources/WKInternalsNotes/Documentation.docc/UIProcess/API/Cocoa/<HeaderName>/

and produces a symbol graph JSON in:
  - Sources/WKInternalsNotes/Documentation.docc/SymbolGraphs/WKInternalsNotes.WKAPI.symbols.json

The symbols are synthetic: they exist only so DocC can render per-entry pages as symbol
reference pages (e.g. "Instance Property" labels and availability badges).
"""

from __future__ import annotations

import argparse

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCC_ROOT = REPO_ROOT / "Sources" / "WKInternalsNotes" / "Documentation.docc"
COCOA_API_ROOT = DOCC_ROOT / "UIProcess" / "API" / "Cocoa"
OUTPUT_DIR = DOCC_ROOT / "SymbolGraphs"
OUTPUT_PATH = OUTPUT_DIR / "WKInternalsNotes.WKAPI.symbols.json"

MODULE_NAME = "WKInternalsNotes"
PRECISE_ID_PREFIX = "wkapi"

def container_symbol_name(header_container_name: str) -> str:
    """Map a header-based container name to the DocC symbol container name.

    Example:
      - WKPreferencesPrivate -> WKPreferences
      - WKWebViewConfigurationPrivate -> WKWebViewConfiguration
    """
    if header_container_name.startswith("WK") and header_container_name.endswith("Private"):
        return header_container_name[: -len("Private")]
    return header_container_name


def discover_header_containers() -> dict[str, Path]:
    containers: dict[str, Path] = {}

    # Header overview pages (one-per-header): UIProcess/API/Cocoa/<HeaderName>.h.md
    for header_page in sorted(COCOA_API_ROOT.glob("*.h.md")):
        header_container_name = header_page.name[: -len(".h.md")]
        container_name = container_symbol_name(header_container_name)
        containers.setdefault(container_name, COCOA_API_ROOT / header_container_name)

    # Entry directories: UIProcess/API/Cocoa/<HeaderName>/...
    for directory in sorted(COCOA_API_ROOT.iterdir()):
        if not directory.is_dir() or directory.name.startswith("."):
            continue
        if next(directory.rglob("*.md"), None) is None:
            continue
        container_name = container_symbol_name(directory.name)
        containers.setdefault(container_name, directory)

    return dict(sorted(containers.items()))


SWIFT_PRECISE_TYPE_IDS: dict[str, str] = {
    "Bool": "s:Sb",
    "Int": "s:Si",
    "UInt": "s:Su",
    "String": "s:SS",
    "Double": "s:Sd",
    "Float": "s:Sf",
}

OBJC_TO_SWIFT_BRIDGED_TYPE_NAMES: dict[str, str] = {
    "NSURL": "URL",
    "NSURLRequest": "URLRequest",
    "NSURLResponse": "URLResponse",
    "NSHTTPURLResponse": "HTTPURLResponse",
    "NSData": "Data",
    "NSDate": "Date",
    "NSError": "Error",
    "NSIndexPath": "IndexPath",
    "NSNotification": "Notification",
    "NSLocale": "Locale",
    "NSTimeZone": "TimeZone",
    "NSUUID": "UUID",
}

OBJC_BLOCK_TYPEALIASES: dict[str, list[str]] = {
    "dispatch_block_t": [],
    "NSAttributedStringCompletionHandler": [
        "NSAttributedString * _Nullable",
        "NSDictionary<NSAttributedStringDocumentAttributeKey, id> * _Nullable",
        "NSError * _Nullable",
    ],
}

C_TYPE_SWIFT_NAME_MAP: dict[str, str] = {
    "size_t": "Int",
    "pid_t": "Int32",
    "int8_t": "Int8",
    "int16_t": "Int16",
    "int32_t": "Int32",
    "int64_t": "Int64",
    "uint8_t": "UInt8",
    "uint16_t": "UInt16",
    "uint32_t": "UInt32",
    "uint64_t": "UInt64",
}

OBJC_PRESERVED_TYPE_NAMES: set[str] = {
    "audit_token_t",
}


PLATFORM_DOMAIN_MAP: dict[str, str] = {
    "macos": "macOS",
    "ios": "iOS",
    "tvos": "tvOS",
    "watchos": "watchOS",
    "visionos": "visionOS",
    "maccatalyst": "macCatalyst",
}


@dataclass(frozen=True)
class SwiftType:
    name: str
    precise_identifier: str | None = None


def _fragment(kind: str, spelling: str, *, precise_identifier: str | None = None) -> dict[str, Any]:
    fragment: dict[str, Any] = {"kind": kind, "spelling": spelling}
    if precise_identifier is not None:
        fragment["preciseIdentifier"] = precise_identifier
    return fragment


def _type_fragment(swift_type: SwiftType) -> dict[str, Any]:
    return _fragment(
        "typeIdentifier",
        swift_type.name,
        precise_identifier=swift_type.precise_identifier,
    )


def _make_precise_id(*path_components: str) -> str:
    joined = "/".join(path_components)
    return f"{PRECISE_ID_PREFIX}:{MODULE_NAME}/{joined}"


def _split_top_level_commas(text: str) -> list[str]:
    parts: list[str] = []
    buf: list[str] = []
    depth = 0
    in_string = False
    escape = False
    for ch in text:
        if in_string:
            buf.append(ch)
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
            buf.append(ch)
            continue
        if ch == "(":
            depth += 1
            buf.append(ch)
            continue
        if ch == ")":
            depth = max(depth - 1, 0)
            buf.append(ch)
            continue
        if ch == "," and depth == 0:
            part = "".join(buf).strip()
            if part:
                parts.append(part)
            buf = []
            continue
        buf.append(ch)

    tail = "".join(buf).strip()
    if tail:
        parts.append(tail)
    return parts


def _split_top_level_commas_in_types(text: str) -> list[str]:
    parts: list[str] = []
    buf: list[str] = []
    paren_depth = 0
    angle_depth = 0
    in_string = False
    escape = False

    for ch in text:
        if in_string:
            buf.append(ch)
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
            buf.append(ch)
            continue
        if ch == "(":
            paren_depth += 1
            buf.append(ch)
            continue
        if ch == ")":
            paren_depth = max(paren_depth - 1, 0)
            buf.append(ch)
            continue
        if ch == "<":
            angle_depth += 1
            buf.append(ch)
            continue
        if ch == ">":
            angle_depth = max(angle_depth - 1, 0)
            buf.append(ch)
            continue
        if ch == "," and paren_depth == 0 and angle_depth == 0:
            part = "".join(buf).strip()
            if part:
                parts.append(part)
            buf = []
            continue

        buf.append(ch)

    tail = "".join(buf).strip()
    if tail:
        parts.append(tail)
    return parts


def _find_matching_paren(text: str, open_index: int) -> int | None:
    depth = 0
    for i in range(open_index, len(text)):
        ch = text[i]
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                return i
    return None


def _find_matching_angle(text: str, open_index: int) -> int | None:
    depth = 0
    for i in range(open_index, len(text)):
        ch = text[i]
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
            if depth == 0:
                return i
    return None


def _extract_wk_api_macros(text: str) -> list[tuple[str, str]]:
    macros: list[tuple[str, str]] = []
    i = 0
    while True:
        m = re.search(r"\b(WK_API_[A-Z0-9_]+)\s*\(", text[i:])
        if not m:
            break
        macro = m.group(1)
        open_paren = i + m.end(0) - 1
        close_paren = _find_matching_paren(text, open_paren)
        if close_paren is None:
            break
        args = text[open_paren + 1 : close_paren]
        macros.append((macro, args))
        i = close_paren + 1
    return macros


def _parse_version(version_text: str) -> dict[str, int] | None:
    v = version_text.strip()
    if not re.fullmatch(r"\d+(?:\.\d+){0,2}", v):
        return None
    parts = [int(p) for p in v.split(".")]
    version: dict[str, int] = {"major": parts[0], "minor": parts[1] if len(parts) >= 2 else 0}
    if len(parts) >= 3:
        version["patch"] = parts[2]
    return version


def _parse_platform_spec(spec: str) -> tuple[str, list[str]] | None:
    m = re.fullmatch(r"([A-Za-z0-9_]+)\s*\(\s*(.*)\s*\)", spec.strip())
    if not m:
        return None
    platform_key = m.group(1).lower()
    args = _split_top_level_commas(m.group(2))
    return platform_key, args


def _availability_from_objc_declaration(objc_declaration: str) -> list[dict[str, Any]]:
    availability_by_domain: dict[str, dict[str, Any]] = {}

    for macro, args in _extract_wk_api_macros(objc_declaration):
        parts = _split_top_level_commas(args)

        if macro == "WK_API_AVAILABLE":
            for part in parts:
                parsed = _parse_platform_spec(part)
                if not parsed:
                    continue
                platform_key, spec_args = parsed
                domain = PLATFORM_DOMAIN_MAP.get(platform_key)
                if domain is None or len(spec_args) < 1:
                    continue
                introduced = _parse_version(spec_args[0])
                if introduced is None:
                    continue
                entry = availability_by_domain.setdefault(domain, {"domain": domain})
                entry.setdefault("introduced", introduced)

        elif macro == "WK_API_UNAVAILABLE":
            for part in parts:
                platform_key = part.strip().lower()
                domain = PLATFORM_DOMAIN_MAP.get(platform_key)
                if domain is None:
                    continue
                entry = availability_by_domain.setdefault(domain, {"domain": domain})
                entry["isUnconditionallyUnavailable"] = True

        elif macro in {"WK_API_DEPRECATED", "WK_API_DEPRECATED_WITH_REPLACEMENT"}:
            if not parts:
                continue
            raw_message = parts[0].strip()
            message = raw_message.strip("\"") if raw_message.startswith("\"") else raw_message
            if macro == "WK_API_DEPRECATED_WITH_REPLACEMENT":
                message = f"use {message}" if message else message

            for part in parts[1:]:
                parsed = _parse_platform_spec(part)
                if not parsed:
                    continue
                platform_key, spec_args = parsed
                domain = PLATFORM_DOMAIN_MAP.get(platform_key)
                if domain is None or len(spec_args) < 1:
                    continue
                introduced = _parse_version(spec_args[0])
                deprecated = _parse_version(spec_args[1]) if len(spec_args) >= 2 else None

                entry = availability_by_domain.setdefault(domain, {"domain": domain})
                if introduced is not None:
                    entry.setdefault("introduced", introduced)
                if deprecated is not None:
                    entry["deprecated"] = deprecated
                if message:
                    entry["message"] = message

    return list(availability_by_domain.values())


def _objc_type_to_swift(objc_type: str) -> SwiftType:
    s = objc_type.strip()
    if not s:
        return SwiftType("Any")

    s_no_qual = s
    s_no_qual = re.sub(r"\b(_Nullable|_Nonnull|_Null_unspecified|nullable|nonnull|null_unspecified|__kindof|inout)\b", "", s_no_qual)
    s_no_qual = re.sub(r"\b(__unsafe_unretained|__strong|__weak|__autoreleasing)\b", "", s_no_qual)
    s_no_qual = re.sub(r"\b(const|volatile)\b", "", s_no_qual)
    s_no_qual = re.sub(r"\s+", " ", s_no_qual).strip()

    alias_params = OBJC_BLOCK_TYPEALIASES.get(s_no_qual)
    if alias_params is not None:
        swift_params = [_objc_type_to_swift(param).name for param in alias_params]
        return SwiftType(f"({', '.join(swift_params)}) -> Void")

    if re.match(r"^void\s*\*$", s_no_qual):
        return SwiftType("UnsafeMutableRawPointer")

    # Translate WebKit's C++ CompletionHandler into a Swift closure when possible.
    # Example:
    #   CompletionHandler<void(BOOL, NSURL *)>&& -> (Bool, URL) -> Void
    if "CompletionHandler" in s:
        m = re.search(r"\bCompletionHandler\s*<", s)
        if m:
            open_index = s.find("<", m.start())
            close_index = _find_matching_angle(s, open_index) if open_index != -1 else None
            if close_index is not None:
                templ = s[open_index + 1 : close_index].strip()
                m_sig = re.match(r"^void\s*\(\s*(.*?)\s*\)\s*$", templ, flags=re.S)
                if m_sig:
                    params_text = m_sig.group(1).strip()
                    params: list[str] = []
                    if params_text and params_text != "void":
                        for part in _split_top_level_commas_in_types(params_text):
                            params.append(_objc_type_to_swift(part).name)
                    return SwiftType(f"({', '.join(params)}) -> Void")
                if templ == "void":
                    return SwiftType("() -> Void")
        return SwiftType("Any")

    # Translate WTF::Function (often imported as `Function<...>`) into a Swift closure when possible.
    # Example:
    #   Function<BOOL(UIScrollView *)>&& -> (UIScrollView) -> Bool
    if "Function" in s:
        m = re.search(r"\bFunction\s*<", s)
        if m:
            open_index = s.find("<", m.start())
            close_index = _find_matching_angle(s, open_index) if open_index != -1 else None
            if close_index is not None:
                templ = s[open_index + 1 : close_index].strip()
                m_sig = re.match(r"^(.+?)\(\s*(.*?)\s*\)\s*$", templ, flags=re.S)
                if m_sig:
                    ret_text = m_sig.group(1).strip()
                    params_text = m_sig.group(2).strip()

                    swift_return = "Void" if ret_text in {"", "void"} else _objc_type_to_swift(ret_text).name
                    params: list[str] = []
                    if params_text and params_text != "void":
                        for part in _split_top_level_commas_in_types(params_text):
                            params.append(_objc_type_to_swift(part).name)
                    return SwiftType(f"({', '.join(params)}) -> {swift_return}")
        return SwiftType("Any")

    # C++ types leaked into Objective-C++ headers (.h/.mm) are common in UIProcess internals.
    # Keep the original spelling so DocC shows the internal type names.
    if "::" in s_no_qual:
        cpp_spelling = re.sub(r"\s*[\*&]+$", "", s_no_qual).strip()
        return SwiftType(cpp_spelling)

    # Preserve protocol-qualified Objective-C "id<...>" as a protocol type rather than "Any".
    #
    # Examples:
    #   - id<NSSecureCoding> -> NSSecureCoding
    #   - id<WKURLSchemeHandler> -> WKURLSchemeHandler
    #   - id<NSSecureCoding, NSCopying> -> NSSecureCoding & NSCopying
    m_id_proto = re.match(r"^id\s*<\s*(.+?)\s*>$", s_no_qual)
    if m_id_proto:
        raw = m_id_proto.group(1).strip()
        parts = _split_top_level_commas_in_types(raw)
        protos: list[str] = []
        for part in parts:
            m_name = re.search(r"\b([A-Za-z_][A-Za-z0-9_]*)\b", part.strip())
            if not m_name:
                continue
            name = m_name.group(1)
            protos.append(OBJC_TO_SWIFT_BRIDGED_TYPE_NAMES.get(name, name))
        if protos:
            return SwiftType(" & ".join(protos))

    if s == "instancetype":
        return SwiftType("Self")
    if s == "id":
        return SwiftType("Any")
    if s == "Class":
        return SwiftType("AnyClass")
    if s == "SEL":
        return SwiftType("Selector")

    # Objective-C blocks: "void (^)(...)" -> "(...) -> Void"
    m_block = re.search(r"\(\s*\^\s*", s)
    if m_block:
        block_open = m_block.start()
        block_close = _find_matching_paren(s, block_open)
        if block_close is not None:
            i = block_close + 1
            while i < len(s) and s[i].isspace():
                i += 1
            if i < len(s) and s[i] == "(":
                params_open = i
                params_close = _find_matching_paren(s, params_open)
                if params_close is not None:
                    objc_return_type = s[:block_open].strip()
                    objc_params = s[params_open + 1 : params_close].strip()

                    swift_return = "Void" if objc_return_type in {"", "void"} else _objc_type_to_swift(objc_return_type).name
                    swift_params: list[str] = []
                    if objc_params and objc_params != "void":
                        for part in _split_top_level_commas_in_types(objc_params):
                            swift_params.append(_objc_type_to_swift(part).name)

                    return SwiftType(f"({', '.join(swift_params)}) -> {swift_return}")

    normalized = s_no_qual
    normalized = normalized.replace("*", " ")
    normalized = re.sub(r"<[^>]+>", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()

    if normalized in {"instancetype"}:
        return SwiftType("Self")
    if normalized in {"id"}:
        return SwiftType("Any")
    if normalized in {"Class"}:
        return SwiftType("AnyClass")
    if normalized in {"SEL"}:
        return SwiftType("Selector")

    mapped = C_TYPE_SWIFT_NAME_MAP.get(normalized)
    if mapped is not None:
        return SwiftType(mapped, SWIFT_PRECISE_TYPE_IDS.get(mapped))
    if normalized in OBJC_PRESERVED_TYPE_NAMES:
        return SwiftType(normalized)

    if re.search(r"\bBOOL\b|\bbool\b", normalized):
        return SwiftType("Bool", SWIFT_PRECISE_TYPE_IDS["Bool"])
    if re.search(r"\bNSUInteger\b|\bunsigned\b", normalized):
        return SwiftType("UInt", SWIFT_PRECISE_TYPE_IDS["UInt"])
    if re.search(r"\bNSInteger\b|\bint\b|\blong\b", normalized):
        return SwiftType("Int", SWIFT_PRECISE_TYPE_IDS["Int"])
    if re.search(r"\bfloat\b", normalized):
        return SwiftType("Float", SWIFT_PRECISE_TYPE_IDS["Float"])
    if re.search(r"\bdouble\b|\bCGFloat\b|\bNSTimeInterval\b", normalized):
        return SwiftType("Double", SWIFT_PRECISE_TYPE_IDS["Double"])
    if re.search(r"\bNSString\b", normalized):
        return SwiftType("String", SWIFT_PRECISE_TYPE_IDS["String"])

    for name in re.findall(r"\b([A-Za-z_][A-Za-z0-9_]*)\b", normalized):
        if name in {"struct", "enum", "union"}:
            continue
        mapped = OBJC_TO_SWIFT_BRIDGED_TYPE_NAMES.get(name)
        if mapped is not None:
            return SwiftType(mapped)
        if name.startswith(("_WK", "WK")):
            return SwiftType(name)
        if name[:1].isupper() or name.startswith("_"):
            return SwiftType(name)
        break

    return SwiftType("Any")


def _extract_first_objc_code_block(markdown: str) -> str | None:
    lines = markdown.splitlines()
    in_block = False
    buf: list[str] = []
    for line in lines:
        if not in_block:
            if line.strip() == "```objective-c":
                in_block = True
            continue
        if line.strip() == "```":
            return "\n".join(buf).strip() or None
        buf.append(line)
    return None


def _condense_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _parse_property_symbol(objc_decl: str) -> tuple[str, SwiftType]:
    line = _condense_whitespace(objc_decl)
    line = re.split(r"\bWK_API_", line)[0].rstrip(";").strip()
    line = _strip_trailing_objc_attributes(line)
    line = re.sub(r"^@property\s*\([^)]*\)\s*", "", line)
    line = re.sub(r"^@property\s*", "", line)

    m_block = re.search(r"\(\s*\^\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)", line)
    if m_block:
        name = m_block.group(1)
        return name, _objc_type_to_swift(line)

    m_name = re.search(r"([A-Za-z_][A-Za-z0-9_]*)\s*$", line)
    if not m_name:
        raise ValueError(f"Unrecognized property declaration: {objc_decl!r}")
    name = m_name.group(1)
    objc_type = line[: m_name.start()].strip()
    if not objc_type:
        raise ValueError(f"Unrecognized property declaration: {objc_decl!r}")
    return name, _objc_type_to_swift(objc_type)


@dataclass(frozen=True)
class MethodSig:
    kind: str  # "instance" | "type"
    base_name: str
    path_component: str
    return_type: SwiftType | None
    params: list[tuple[str, str, SwiftType]]  # (external_label, internal_name, type)
    is_init: bool = False


def _swift_lowercase_identifier(text: str) -> str:
    if not text:
        return text
    for i, ch in enumerate(text):
        if ch.islower():
            if i == 0:
                return text
            if i == 1:
                return text[0].lower() + text[1:]
            return text[: i - 1].lower() + text[i - 1 :]
    return text.lower()


def _swiftify_init_label(label: str) -> str:
    if not label.startswith("init"):
        return label
    tail = label[len("init") :]
    if tail.startswith("With"):
        tail = tail[len("With") :]
    if not tail:
        return "_"
    return _swift_lowercase_identifier(tail)


def _parse_method_symbol(objc_decl: str) -> MethodSig:
    line = _condense_whitespace(objc_decl)
    kind = "type" if line.lstrip().startswith("+") else "instance"
    line = re.split(r"\bWK_API_", line)[0].rstrip(";").strip()
    line = _strip_trailing_objc_attributes(line)

    if not (line.lstrip().startswith("-") or line.lstrip().startswith("+")):
        raise ValueError(f"Unrecognized method declaration: {objc_decl!r}")

    return_type: SwiftType | None
    open_paren = line.find("(")
    if open_paren == -1:
        raise ValueError(f"Unrecognized method declaration: {objc_decl!r}")
    close_paren = _find_matching_paren(line, open_paren)
    if close_paren is None:
        raise ValueError(f"Unrecognized method declaration: {objc_decl!r}")

    objc_return_type = line[open_paren + 1 : close_paren].strip()
    rest = line[close_paren + 1 :].strip()

    return_type = None if objc_return_type == "void" else _objc_type_to_swift(objc_return_type)

    params: list[tuple[str, str, SwiftType]] = []
    if ":" not in rest:
        base_name = rest.split()[0]
        is_init = kind == "instance" and base_name.startswith("init")
        if is_init:
            return MethodSig(kind, "init", "init()", None, params, is_init=True)
        return MethodSig(kind, base_name, f"{base_name}()", return_type, params)

    segments: list[tuple[str, str, SwiftType]] = []
    i = 0
    while True:
        colon_index = rest.find(":", i)
        if colon_index == -1:
            break

        label = rest[i:colon_index].strip()
        if not label:
            raise ValueError(f"Unrecognized method declaration: {objc_decl!r}")

        j = colon_index + 1
        while j < len(rest) and rest[j].isspace():
            j += 1
        if j >= len(rest) or rest[j] != "(":
            raise ValueError(f"Unrecognized method declaration: {objc_decl!r}")

        type_open = j
        type_close = _find_matching_paren(rest, type_open)
        if type_close is None:
            raise ValueError(f"Unrecognized method declaration: {objc_decl!r}")

        objc_param_type = rest[type_open + 1 : type_close].strip()

        k = type_close + 1
        while k < len(rest) and rest[k].isspace():
            k += 1

        m_name = re.match(r"([A-Za-z_][A-Za-z0-9_]*)", rest[k:])
        if not m_name:
            raise ValueError(f"Unrecognized method declaration: {objc_decl!r}")
        internal_name = m_name.group(1)
        k += m_name.end()

        segments.append((label, internal_name, _objc_type_to_swift(objc_param_type)))

        i = k
        while i < len(rest) and rest[i].isspace():
            i += 1

    if not segments:
        base_name = rest.split()[0]
        return MethodSig(kind, base_name, f"{base_name}()", return_type, params)

    base_name = segments[0][0]
    is_init = kind == "instance" and base_name.startswith("init")
    if is_init:
        base_name = "init"
    for idx, (label, internal_name, swift_type) in enumerate(segments):
        if is_init:
            external_label = _swiftify_init_label(label) if idx == 0 else label
        else:
            external_label = "_" if idx == 0 else label
        params.append((external_label, internal_name, swift_type))

    labels = [p[0] + ":" for p in params]
    path_component = f"{base_name}({''.join(labels)})"
    return MethodSig(kind, base_name, path_component, None if is_init else return_type, params, is_init=is_init)


def _parse_enum_symbol(objc_decl: str) -> tuple[str, list[str]]:
    m = re.search(r"typedef\s+NS_(?:ENUM|OPTIONS)\s*\([^,]+,\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)", objc_decl)
    if not m:
        raise ValueError(f"Unrecognized enum declaration: {objc_decl!r}")
    enum_name = m.group(1)

    brace_open = objc_decl.find("{")
    brace_close = objc_decl.rfind("}")
    if brace_open == -1 or brace_close == -1 or brace_close <= brace_open:
        return enum_name, []
    body = objc_decl[brace_open + 1 : brace_close]

    cases: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        stripped = stripped.split("//", 1)[0].strip()
        stripped = stripped.rstrip(",").strip()
        if not stripped:
            continue
        m_case = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\b", stripped)
        if not m_case:
            continue
        cases.append(m_case.group(1))
    return enum_name, cases


def _strip_trailing_objc_attributes(line: str) -> str:
    # e.g.
    #   - "... Foo NS_SWIFT_NONISOLATED"
    #   - "... Foo NS_SWIFT_NAME(Bar)"
    #   - "... Foo API_AVAILABLE(macos(14.0), ios(17.0))"
    s = line.strip()
    while True:
        s = s.rstrip()
        if not s:
            return s

        if s.endswith(")"):
            depth = 0
            open_index: int | None = None
            for i in range(len(s) - 1, -1, -1):
                ch = s[i]
                if ch == ")":
                    depth += 1
                elif ch == "(":
                    depth -= 1
                    if depth == 0:
                        open_index = i
                        break
            if open_index is None:
                break

            j = open_index - 1
            while j >= 0 and s[j].isspace():
                j -= 1
            k = j
            while k >= 0 and (s[k].isalnum() or s[k] == "_"):
                k -= 1
            ident = s[k + 1 : j + 1]
            if ident.startswith(("NS_", "WK_", "API_")):
                s = s[: k + 1].rstrip()
                continue
            break

        head, sep, tail = s.rpartition(" ")
        if not sep:
            break
        if tail.startswith(("NS_", "WK_", "API_")):
            s = head
            continue
        break

    return s.strip()


def _parse_extern_symbol(objc_decl: str) -> tuple[str, SwiftType]:
    line = _condense_whitespace(objc_decl)
    line = re.split(r"\bWK_API_", line)[0].rstrip(";").strip()
    line = _strip_trailing_objc_attributes(line)
    line = re.sub(r"^(extern|FOUNDATION_EXPORT|WK_EXTERN)\s+", "", line).strip()

    m_block = re.search(r"\(\s*\^\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)", line)
    if m_block:
        name = m_block.group(1)
        return name, _objc_type_to_swift(line)

    m_name = re.search(r"\b([A-Za-z_][A-Za-z0-9_]*)\b\s*$", line)
    if not m_name:
        raise ValueError(f"Unrecognized extern declaration: {objc_decl!r}")
    name = m_name.group(1)
    objc_type = line[: m_name.start()].strip()
    return name, _objc_type_to_swift(objc_type)


def _parse_typedef_symbol(objc_decl: str) -> tuple[str, SwiftType]:
    line = _condense_whitespace(objc_decl)
    line = re.split(r"\bWK_API_", line)[0].rstrip(";").strip()
    line = _strip_trailing_objc_attributes(line)
    if not line.startswith("typedef "):
        raise ValueError(f"Unrecognized typedef declaration: {objc_decl!r}")
    if "NS_ENUM" in line or "NS_OPTIONS" in line:
        raise ValueError(f"Unrecognized typedef declaration: {objc_decl!r}")
    line = line[len("typedef ") :].strip()

    m_block = re.search(r"\(\s*\^\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)", line)
    if m_block:
        name = m_block.group(1)
        return name, _objc_type_to_swift(line)

    m_ptr = re.search(r"\(\s*\*\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)", line)
    if m_ptr:
        return m_ptr.group(1), SwiftType("Any")

    m_name = re.search(r"\b([A-Za-z_][A-Za-z0-9_]*)\b\s*$", line)
    if not m_name:
        raise ValueError(f"Unrecognized typedef declaration: {objc_decl!r}")
    name = m_name.group(1)
    objc_type = line[: m_name.start()].strip()
    return name, _objc_type_to_swift(objc_type) if objc_type else SwiftType("Any")


def _parse_protocol_symbol(objc_decl: str) -> str:
    line = _condense_whitespace(objc_decl.splitlines()[0])
    m = re.match(r"^@protocol\s+([A-Za-z_][A-Za-z0-9_]*)\b", line)
    if not m:
        raise ValueError(f"Unrecognized protocol declaration: {objc_decl!r}")
    return m.group(1)


def _parse_interface_symbol(objc_decl: str) -> str:
    line = _condense_whitespace(objc_decl.splitlines()[0])
    m = re.match(r"^@interface\s+([A-Za-z_][A-Za-z0-9_]*)\b", line)
    if not m:
        raise ValueError(f"Unrecognized interface declaration: {objc_decl!r}")
    return m.group(1)

HEADER_CONTAINER_KIND = {"identifier": "swift.class", "displayName": "Class"}
HEADER_CONTAINER_KEYWORD = "class"


def _make_header_container_symbol(type_name: str) -> dict[str, Any]:
    return {
        "accessLevel": "public",
        "kind": HEADER_CONTAINER_KIND,
        "identifier": {"precise": _make_precise_id(type_name), "interfaceLanguage": "swift"},
        "pathComponents": [type_name],
        "names": {
            "title": type_name,
            "navigator": [_fragment("identifier", type_name)],
            "subHeading": [
                _fragment("keyword", HEADER_CONTAINER_KEYWORD),
                _fragment("text", " "),
                _fragment("identifier", type_name),
            ],
        },
        "declarationFragments": [
            _fragment("keyword", HEADER_CONTAINER_KEYWORD),
            _fragment("text", " "),
            _fragment("identifier", type_name),
        ],
    }


def _make_nested_class_symbol(container: str, type_name: str, *, availability: list[dict[str, Any]]) -> dict[str, Any]:
    symbol = {
        "accessLevel": "public",
        "kind": {"identifier": "swift.class", "displayName": "Class"},
        "identifier": {"precise": _make_precise_id(container, type_name), "interfaceLanguage": "swift"},
        "pathComponents": [container, type_name],
        "names": {
            "title": type_name,
            "navigator": [_fragment("identifier", type_name)],
            "subHeading": [
                _fragment("keyword", "class"),
                _fragment("text", " "),
                _fragment("identifier", type_name),
            ],
        },
        "declarationFragments": [
            _fragment("keyword", "class"),
            _fragment("text", " "),
            _fragment("identifier", type_name),
        ],
    }
    if availability:
        symbol["availability"] = availability
    return symbol


def _make_protocol_symbol(container: str, name: str, *, availability: list[dict[str, Any]]) -> dict[str, Any]:
    decl = [
        _fragment("keyword", "protocol"),
        _fragment("text", " "),
        _fragment("identifier", name),
    ]
    symbol: dict[str, Any] = {
        "accessLevel": "public",
        "kind": {"identifier": "swift.protocol", "displayName": "Protocol"},
        "identifier": {"precise": _make_precise_id(container, name), "interfaceLanguage": "swift"},
        "pathComponents": [container, name],
        "names": {"title": name, "navigator": [_fragment("identifier", name)], "subHeading": decl},
        "declarationFragments": decl,
    }
    if availability:
        symbol["availability"] = availability
    return symbol


def _make_typealias_symbol(container: str, name: str, swift_type: SwiftType, *, availability: list[dict[str, Any]]) -> dict[str, Any]:
    decl = [
        _fragment("keyword", "typealias"),
        _fragment("text", " "),
        _fragment("identifier", name),
        _fragment("text", " = "),
        _type_fragment(swift_type),
    ]
    symbol: dict[str, Any] = {
        "accessLevel": "public",
        "kind": {"identifier": "swift.typealias", "displayName": "Type Alias"},
        "identifier": {"precise": _make_precise_id(container, name), "interfaceLanguage": "swift"},
        "pathComponents": [container, name],
        "names": {"title": name, "subHeading": decl},
        "declarationFragments": decl,
    }
    if availability:
        symbol["availability"] = availability
    return symbol


def _make_global_var_symbol(container: str, name: str, swift_type: SwiftType, *, availability: list[dict[str, Any]]) -> dict[str, Any]:
    decl = [
        _fragment("keyword", "let"),
        _fragment("text", " "),
        _fragment("identifier", name),
        _fragment("text", ": "),
        _type_fragment(swift_type),
    ]
    symbol: dict[str, Any] = {
        "accessLevel": "public",
        "kind": {"identifier": "swift.var", "displayName": "Global Variable"},
        "identifier": {"precise": _make_precise_id(container, name), "interfaceLanguage": "swift"},
        "pathComponents": [container, name],
        "names": {"title": name, "subHeading": decl},
        "declarationFragments": decl,
    }
    if availability:
        symbol["availability"] = availability
    return symbol


def _make_property_symbol(container: str, name: str, swift_type: SwiftType, *, availability: list[dict[str, Any]]) -> dict[str, Any]:
    decl = [
        _fragment("keyword", "var"),
        _fragment("text", " "),
        _fragment("identifier", name),
        _fragment("text", ": "),
        _type_fragment(swift_type),
    ]
    symbol: dict[str, Any] = {
        "accessLevel": "public",
        "kind": {"identifier": "swift.property", "displayName": "Instance Property"},
        "identifier": {"precise": _make_precise_id(container, name), "interfaceLanguage": "swift"},
        "pathComponents": [container, name],
        "names": {"title": name, "subHeading": decl},
        "declarationFragments": decl,
    }
    if availability:
        symbol["availability"] = availability
    return symbol


def _make_method_symbol(container: str, sig: MethodSig, *, availability: list[dict[str, Any]]) -> dict[str, Any]:
    if sig.is_init:
        decl: list[dict[str, Any]] = []
        decl.append(_fragment("keyword", "init"))
        decl.append(_fragment("text", "("))

        for idx, (external, internal, swift_type) in enumerate(sig.params):
            if idx > 0:
                decl.append(_fragment("text", ", "))
            if external == "_" or external != internal:
                decl.append(_fragment("externalParam", external))
                decl.append(_fragment("text", " "))
                decl.append(_fragment("internalParam", internal))
            else:
                decl.append(_fragment("externalParam", external))
            decl.append(_fragment("text", ": "))
            decl.append(_type_fragment(swift_type))

        decl.append(_fragment("text", ")"))

        sub: list[dict[str, Any]] = []
        sub.append(_fragment("keyword", "init"))
        sub.append(_fragment("text", "("))
        for idx, (external, _internal, swift_type) in enumerate(sig.params):
            if idx > 0:
                sub.append(_fragment("text", ", "))
            if idx == 0 and external == "_":
                sub.append(_type_fragment(swift_type))
            else:
                sub.append(_fragment("externalParam", external))
                sub.append(_fragment("text", ": "))
                sub.append(_type_fragment(swift_type))
        sub.append(_fragment("text", ")"))

        symbol: dict[str, Any] = {
            "accessLevel": "public",
            "kind": {"identifier": "swift.init", "displayName": "Initializer"},
            "identifier": {"precise": _make_precise_id(container, sig.path_component), "interfaceLanguage": "swift"},
            "pathComponents": [container, sig.path_component],
            "names": {"title": sig.path_component, "subHeading": sub},
            "declarationFragments": decl,
            "functionSignature": {
                "parameters": [
                    {
                        "name": internal,
                        "declarationFragments": [
                            _fragment("identifier", internal),
                            _fragment("text", ": "),
                            _type_fragment(swift_type),
                        ],
                    }
                    for (_external, internal, swift_type) in sig.params
                ],
            },
        }
        if availability:
            symbol["availability"] = availability
        return symbol

    kind_id = "swift.method" if sig.kind == "instance" else "swift.type.method"
    kind_display = "Instance Method" if sig.kind == "instance" else "Type Method"

    decl: list[dict[str, Any]] = []
    if sig.kind == "type":
        decl.append(_fragment("keyword", "static"))
        decl.append(_fragment("text", " "))
    decl.append(_fragment("keyword", "func"))
    decl.append(_fragment("text", " "))
    decl.append(_fragment("identifier", sig.base_name))
    decl.append(_fragment("text", "("))

    for idx, (external, internal, swift_type) in enumerate(sig.params):
        if idx > 0:
            decl.append(_fragment("text", ", "))
        if external == "_" or external != internal:
            decl.append(_fragment("externalParam", external))
            decl.append(_fragment("text", " "))
            decl.append(_fragment("internalParam", internal))
        else:
            decl.append(_fragment("externalParam", external))
        decl.append(_fragment("text", ": "))
        decl.append(_type_fragment(swift_type))

    decl.append(_fragment("text", ")"))
    if sig.return_type is not None:
        decl.append(_fragment("text", " -> "))
        decl.append(_type_fragment(sig.return_type))

    sub: list[dict[str, Any]] = []
    sub.append(_fragment("keyword", "func"))
    sub.append(_fragment("text", " "))
    sub.append(_fragment("identifier", sig.base_name))
    sub.append(_fragment("text", "("))
    for idx, (external, _internal, swift_type) in enumerate(sig.params):
        if idx > 0:
            sub.append(_fragment("text", ", "))
        if idx == 0 and external == "_":
            sub.append(_type_fragment(swift_type))
        else:
            sub.append(_fragment("externalParam", external))
            sub.append(_fragment("text", ": "))
            sub.append(_type_fragment(swift_type))
    sub.append(_fragment("text", ")"))
    if sig.return_type is not None:
        sub.append(_fragment("text", " -> "))
        sub.append(_type_fragment(sig.return_type))

    returns: list[dict[str, Any]]
    if sig.return_type is None:
        returns = [_fragment("text", "()")]
    else:
        returns = [_type_fragment(sig.return_type)]

    symbol: dict[str, Any] = {
        "accessLevel": "public",
        "kind": {"identifier": kind_id, "displayName": kind_display},
        "identifier": {"precise": _make_precise_id(container, sig.path_component), "interfaceLanguage": "swift"},
        "pathComponents": [container, sig.path_component],
        "names": {"title": sig.path_component, "subHeading": sub},
        "declarationFragments": decl,
        "functionSignature": {
            "parameters": [
                {
                    "name": internal,
                    "declarationFragments": [
                        _fragment("identifier", internal),
                        _fragment("text", ": "),
                        _type_fragment(swift_type),
                    ],
                }
                for (_external, internal, swift_type) in sig.params
            ],
            "returns": returns,
        },
    }
    if availability:
        symbol["availability"] = availability
    return symbol


def _make_enum_symbol(container: str, enum_name: str, *, availability: list[dict[str, Any]]) -> dict[str, Any]:
    decl = [
        _fragment("keyword", "enum"),
        _fragment("text", " "),
        _fragment("identifier", enum_name),
    ]
    symbol: dict[str, Any] = {
        "accessLevel": "public",
        "kind": {"identifier": "swift.enum", "displayName": "Enumeration"},
        "identifier": {"precise": _make_precise_id(container, enum_name), "interfaceLanguage": "swift"},
        "pathComponents": [container, enum_name],
        "names": {
            "title": enum_name,
            "navigator": [_fragment("identifier", enum_name)],
            "subHeading": decl,
        },
        "declarationFragments": decl,
    }
    if availability:
        symbol["availability"] = availability
    return symbol


def _make_enum_case_symbol(container: str, enum_name: str, case_name: str, *, availability: list[dict[str, Any]]) -> dict[str, Any]:
    decl = [
        _fragment("keyword", "case"),
        _fragment("text", " "),
        _fragment("identifier", case_name),
    ]
    symbol: dict[str, Any] = {
        "accessLevel": "public",
        "kind": {"identifier": "swift.enum.case", "displayName": "Case"},
        "identifier": {"precise": _make_precise_id(container, enum_name, case_name), "interfaceLanguage": "swift"},
        "pathComponents": [container, enum_name, case_name],
        "names": {"title": f"{enum_name}.{case_name}", "subHeading": decl},
        "declarationFragments": decl,
    }
    if availability:
        symbol["availability"] = availability
    return symbol


def _iter_entry_markdown_files(header_dir: Path) -> Iterable[Path]:
    for path in sorted(header_dir.rglob("*.md")):
        if path.name.endswith(".md") and path.is_file():
            yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help=(
            "Write the legacy symbol graph to this path. "
            "If omitted, the script is disabled to avoid overwriting the primary WKAPI symbol graph."
        ),
    )
    args = parser.parse_args()

    if args.output is None:
        print(
            "error: legacy generator is disabled.\n"
            "  - Use: python3 Scripts/generate_webkit_uiprocess_objc_symbol_graph.py --write-index\n"
            "  - Reason: this legacy script used to write to the same output path and could overwrite WKAPI.\n"
            "  - To run anyway, pass: --output /path/to/file.json",
            file=sys.stderr,
        )
        return 2

    header_containers = discover_header_containers()
    if not header_containers:
        print(f"error: no header containers found under: {COCOA_API_ROOT}", file=sys.stderr)
        return 2

    platform = {
        "architecture": "arm64",
        "vendor": "apple",
        "operatingSystem": {"name": "macosx", "minimumVersion": {"major": 10, "minor": 13}},
    }

    symbols: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []

    for container in header_containers.keys():
        symbols.append(_make_header_container_symbol(container))

    for container, directory in header_containers.items():
        container_id = _make_precise_id(container)

        if not directory.exists():
            print(f"warning: missing entry directory: {directory}", file=sys.stderr)
            continue

        for md_path in _iter_entry_markdown_files(directory):
            markdown = md_path.read_text(encoding="utf-8")
            objc_block = _extract_first_objc_code_block(markdown)
            if objc_block is None:
                continue

            availability = _availability_from_objc_declaration(objc_block)
            first_line = _condense_whitespace(objc_block.splitlines()[0]) if objc_block else ""

            try:
                if "typedef NS_ENUM" in objc_block or "typedef NS_OPTIONS" in objc_block:
                    enum_name, cases = _parse_enum_symbol(objc_block)
                    enum_symbol = _make_enum_symbol(container, enum_name, availability=availability)
                    symbols.append(enum_symbol)
                    relationships.append(
                        {"kind": "memberOf", "source": enum_symbol["identifier"]["precise"], "target": container_id}
                    )

                    enum_id = enum_symbol["identifier"]["precise"]
                    for case_name in cases:
                        case_symbol = _make_enum_case_symbol(
                            container, enum_name, case_name, availability=availability
                        )
                        symbols.append(case_symbol)
                        relationships.append(
                            {"kind": "memberOf", "source": case_symbol["identifier"]["precise"], "target": enum_id}
                        )
                elif first_line.startswith("@property"):
                    name, swift_type = _parse_property_symbol(objc_block)
                    prop_symbol = _make_property_symbol(container, name, swift_type, availability=availability)
                    symbols.append(prop_symbol)
                    relationships.append(
                        {"kind": "memberOf", "source": prop_symbol["identifier"]["precise"], "target": container_id}
                    )
                elif re.match(r"^(extern|FOUNDATION_EXPORT|WK_EXTERN)\b", first_line):
                    name, swift_type = _parse_extern_symbol(objc_block)
                    var_symbol = _make_global_var_symbol(container, name, swift_type, availability=availability)
                    symbols.append(var_symbol)
                    relationships.append(
                        {"kind": "memberOf", "source": var_symbol["identifier"]["precise"], "target": container_id}
                    )
                elif first_line.startswith("typedef"):
                    name, swift_type = _parse_typedef_symbol(objc_block)
                    alias_type = swift_type if swift_type.name != "Any" else SwiftType("Any")
                    alias_symbol = _make_typealias_symbol(container, name, alias_type, availability=availability)
                    symbols.append(alias_symbol)
                    relationships.append(
                        {"kind": "memberOf", "source": alias_symbol["identifier"]["precise"], "target": container_id}
                    )
                elif first_line.startswith("@protocol"):
                    name = _parse_protocol_symbol(objc_block)
                    proto_symbol = _make_protocol_symbol(container, name, availability=availability)
                    symbols.append(proto_symbol)
                    relationships.append(
                        {"kind": "memberOf", "source": proto_symbol["identifier"]["precise"], "target": container_id}
                    )
                elif first_line.startswith("@interface"):
                    name = _parse_interface_symbol(objc_block)
                    class_symbol = _make_nested_class_symbol(container, name, availability=availability)
                    symbols.append(class_symbol)
                    relationships.append(
                        {"kind": "memberOf", "source": class_symbol["identifier"]["precise"], "target": container_id}
                    )
                elif first_line.startswith("-") or first_line.startswith("+"):
                    sig = _parse_method_symbol(objc_block)
                    method_symbol = _make_method_symbol(container, sig, availability=availability)
                    symbols.append(method_symbol)
                    relationships.append(
                        {
                            "kind": "memberOf",
                            "source": method_symbol["identifier"]["precise"],
                            "target": container_id,
                        }
                    )
                else:
                    print(f"warning: unsupported declaration in {md_path}:\n  {first_line}", file=sys.stderr)
            except Exception as e:  # noqa: BLE001
                print(f"warning: failed to parse {md_path}: {e}", file=sys.stderr)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    graph = {
        "metadata": {
            "formatVersion": {"major": 0, "minor": 6, "patch": 0},
            "generator": "WKInternalsNotes synthetic symbol graph generator",
        },
        "module": {"name": MODULE_NAME, "platform": platform},
        "symbols": symbols,
        "relationships": relationships,
    }
    args.output.write_text(json.dumps(graph, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    try:
        rel = args.output.relative_to(REPO_ROOT)
    except ValueError:
        rel = args.output
    print(f"Wrote: {rel} ({len(symbols)} symbols)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
