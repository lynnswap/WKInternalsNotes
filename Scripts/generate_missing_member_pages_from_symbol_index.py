#!/usr/bin/env python3
"""
Generate missing DocC member pages from the synthetic symbol index.

Outputs:
  Sources/WKInternalsNotes/Documentation.docc/UIProcess/API/Cocoa/<Container>/<Entry>.md

Notes:
  - The output directory is based on UIProcess/API/Cocoa headers when available.
  - When no Cocoa header exists for a container, the container name is used as the folder name.
  - Declarations are extracted from UIProcess .h/.m/.mm files (best-effort).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable

import generate_webkitspi_private_symbol_graph as objc


REPO_ROOT = Path(__file__).resolve().parents[1]
REVISION_FILE = REPO_ROOT / "WebKit.revision"
DOCC_ROOT = REPO_ROOT / "Sources" / "WKInternalsNotes" / "Documentation.docc"
INDEX_PATH = DOCC_ROOT / "SymbolGraphs" / "WKInternalsNotes.WKAPI.symbols.index.json"
DOCC_COCOA_DIR = DOCC_ROOT / "UIProcess" / "API" / "Cocoa"

DEFAULT_WEBKIT_CHECKOUT = REPO_ROOT / "References" / "WebKit"
WEBKIT_UI_PROCESS_DIR = Path("Source/WebKit/UIProcess")
WEBKIT_COCOA_HEADERS_DIR = Path("Source/WebKit/UIProcess/API/Cocoa")

WEBKIT_GITHUB_BASE = "https://github.com/WebKit/WebKit"
MODULE_NAME = "WKInternalsNotes"

EXCLUDED_PORT_PATH_PARTS = {
    "glib",
    "gtk",
    "wpe",
    "libwpe",
}


def _read_revision() -> str:
    for line in REVISION_FILE.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        return s
    raise RuntimeError(f"no revision found in: {REVISION_FILE}")


def _webkit_root_from_env() -> Path:
    env = os.environ.get("WKINTERNALS_WEBKIT_CHECKOUT")
    if env:
        return Path(env).expanduser()
    return DEFAULT_WEBKIT_CHECKOUT


def _iter_files(root: Path, *, exts: tuple[str, ...]) -> Iterable[Path]:
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix not in exts:
            continue
        if EXCLUDED_PORT_PATH_PARTS.intersection(path.parts):
            continue
        yield path


def _find_cocoa_header_for_container(webkit_root: Path, container: str) -> Path | None:
    headers_dir = webkit_root / WEBKIT_COCOA_HEADERS_DIR
    candidates = [f"{container}Private.h", f"{container}.h"]
    for name in candidates:
        p = headers_dir / name
        if p.exists():
            return p
    return None


def _entry_filename_for_member(member: str) -> str:
    if "(" not in member:
        return f"{member}.md"
    base = member.split("(", 1)[0]
    inside = member.split("(", 1)[1].rsplit(")", 1)[0]
    labels = [seg for seg in inside.split(":") if seg]
    suffix = [label for label in labels[1:] if label and label != "_"]
    name = base + "".join(f"_{label}" for label in suffix)
    return f"{name}.md"


@dataclass(frozen=True)
class InterfaceBlock:
    type_name: str
    start_line: int
    body_lines: list[str]


_INTERFACE_RE = re.compile(r"^\s*@interface\s+([A-Za-z_][A-Za-z0-9_]*)\b")


def _iter_interface_blocks(lines: list[str]) -> Iterable[InterfaceBlock]:
    i = 0
    while i < len(lines):
        line = lines[i]
        m = _INTERFACE_RE.match(line)
        if not m:
            i += 1
            continue

        type_name = m.group(1)
        start_line = i + 1
        body: list[str] = []
        i += 1
        while i < len(lines):
            if re.match(r"^\s*@end\b", lines[i]):
                break
            body.append(lines[i])
            i += 1
        yield InterfaceBlock(type_name=type_name, start_line=start_line, body_lines=body)

        while i < len(lines) and not re.match(r"^\s*@end\b", lines[i]):
            i += 1
        if i < len(lines):
            i += 1


@dataclass(frozen=True)
class ProtocolBlock:
    name: str
    start_line: int
    header_line: str
    body_lines: list[str]


_PROTOCOL_RE = re.compile(r"^\s*@protocol\b")


def _parse_protocol_names_from_forward_decl(line: str) -> list[str]:
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


def _iter_protocol_blocks(lines: list[str]) -> Iterable[ProtocolBlock]:
    i = 0
    while i < len(lines):
        line = lines[i]
        if not _PROTOCOL_RE.match(line):
            i += 1
            continue

        forward_names = _parse_protocol_names_from_forward_decl(line)
        if forward_names:
            for name in forward_names:
                yield ProtocolBlock(name=name, start_line=i + 1, header_line=line, body_lines=[])
            i += 1
            continue

        try:
            name = objc._parse_protocol_symbol(line)  # noqa: SLF001
        except Exception:
            i += 1
            continue

        start_line = i + 1
        header_line = line
        body: list[str] = []
        i += 1
        while i < len(lines):
            if re.match(r"^\s*@end\b", lines[i]):
                break
            body.append(lines[i])
            i += 1
        yield ProtocolBlock(name=name, start_line=start_line, header_line=header_line, body_lines=body)

        while i < len(lines) and not re.match(r"^\s*@end\b", lines[i]):
            i += 1
        if i < len(lines):
            i += 1


def _iter_semicolon_decls_with_location(
    lines: list[str],
    *,
    starters: tuple[str, ...],
    base_line: int,
) -> Iterable[tuple[int, str]]:
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

        start_line = base_line + i
        buf: list[str] = [line.rstrip("\n")]
        i += 1
        while i < len(lines) and ";" not in buf[-1]:
            buf.append(lines[i].rstrip("\n"))
            if ";" in lines[i]:
                i += 1
                break
            i += 1
        yield start_line, "\n".join(buf).strip()


def _strip_objc_comments(text: str) -> str:
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"//.*", "", text)
    return text


@dataclass(frozen=True)
class DeclLocation:
    file_repo_rel: str
    line: int
    decl: str


@dataclass
class MemberDecls:
    header: DeclLocation | None = None
    implementation: DeclLocation | None = None

    def primary(self) -> DeclLocation | None:
        return self.header or self.implementation

    def references(self) -> list[DeclLocation]:
        refs: list[DeclLocation] = []
        if self.header:
            refs.append(self.header)
        if self.implementation and self.implementation.file_repo_rel != (self.header.file_repo_rel if self.header else None):
            refs.append(self.implementation)
        return refs


def _build_declaration_index(webkit_root: Path) -> dict[str, dict[str, MemberDecls]]:
    ui_process_root = webkit_root / WEBKIT_UI_PROCESS_DIR
    if not ui_process_root.exists():
        raise RuntimeError(f"missing WebKit UIProcess dir: {ui_process_root}")

    index: dict[str, dict[str, MemberDecls]] = {}

    def store_decl(container: str, member: str, location: DeclLocation, *, is_header: bool) -> None:
        entry = index.setdefault(container, {}).setdefault(member, MemberDecls())
        if is_header and entry.header is None:
            entry.header = location
        if not is_header and entry.implementation is None:
            entry.implementation = location

    for path in _iter_files(ui_process_root, exts=(".h", ".m", ".mm")):
        is_header = path.suffix == ".h"
        try:
            raw_lines = path.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
        except Exception:
            continue

        # Protocol members.
        for block in _iter_protocol_blocks(raw_lines):
            if not block.body_lines:
                continue
            for line_no, decl in _iter_semicolon_decls_with_location(
                block.body_lines,
                starters=("@property", "-", "+"),
                base_line=block.start_line,
            ):
                cleaned_decl = _strip_objc_comments(decl)
                first = objc._condense_whitespace(cleaned_decl.splitlines()[0])  # noqa: SLF001
                try:
                    if first.startswith("@property"):
                        name, _ty = objc._parse_property_symbol(cleaned_decl)  # noqa: SLF001
                        store_decl(
                            block.name,
                            name,
                            DeclLocation(str(path.relative_to(webkit_root)), line_no, cleaned_decl),
                            is_header=is_header,
                        )
                    elif first.startswith("-") or first.startswith("+"):
                        sig = objc._parse_method_symbol(cleaned_decl)  # noqa: SLF001
                        store_decl(
                            block.name,
                            sig.path_component,
                            DeclLocation(str(path.relative_to(webkit_root)), line_no, cleaned_decl),
                            is_header=is_header,
                        )
                except Exception:
                    continue

        # Interface members.
        for block in _iter_interface_blocks(raw_lines):
            for line_no, decl in _iter_semicolon_decls_with_location(
                block.body_lines,
                starters=("@property", "-", "+"),
                base_line=block.start_line,
            ):
                cleaned_decl = _strip_objc_comments(decl)
                first = objc._condense_whitespace(cleaned_decl.splitlines()[0])  # noqa: SLF001
                try:
                    if first.startswith("@property"):
                        name, _ty = objc._parse_property_symbol(cleaned_decl)  # noqa: SLF001
                        store_decl(
                            block.type_name,
                            name,
                            DeclLocation(str(path.relative_to(webkit_root)), line_no, cleaned_decl),
                            is_header=is_header,
                        )
                    elif first.startswith("-") or first.startswith("+"):
                        sig = objc._parse_method_symbol(cleaned_decl)  # noqa: SLF001
                        store_decl(
                            block.type_name,
                            sig.path_component,
                            DeclLocation(str(path.relative_to(webkit_root)), line_no, cleaned_decl),
                            is_header=is_header,
                        )
                except Exception:
                    continue

    return index


def _github_blob_url(revision: str, repo_rel: str, *, line: int | None) -> str:
    url = f"{WEBKIT_GITHUB_BASE}/blob/{revision}/{repo_rel}"
    if line is not None:
        url += f"#L{line}"
    return url


def _short_link_text(repo_rel: str, *, line: int | None) -> str:
    base = repo_rel.rsplit("/", 1)[-1]
    return f"`{base}`" if line is None else f"`{base}#L{line}`"


def _render_page(
    *,
    container: str,
    member: str,
    decls: MemberDecls | None,
    revision: str,
) -> str:
    today = date.today().isoformat()
    is_property = "(" not in member

    primary = decls.primary() if decls else None
    objc_decl = primary.decl.strip() if primary else "TODO"

    out: list[str] = []
    out.append(f"# ``{MODULE_NAME}/{container}/{member}``")
    out.append("")
    out.append("実装未調査。")
    out.append("")

    out.append("## Objective-C Declaration")
    out.append("```objective-c")
    out.append(objc_decl)
    out.append("```")
    out.append("")

    if is_property:
        out.append("## Default Value")
        out.append("未調査（初期化経路の確認が必要）。")
        out.append("")

    out.append("## Discussion")
    out.append("実装未調査。宣言と対応実装の確認が必要。")
    out.append("")

    out.append("## References")
    refs = decls.references() if decls else []
    if refs:
        for ref in refs:
            url = _github_blob_url(revision, ref.file_repo_rel, line=ref.line)
            out.append(f"- [{_short_link_text(ref.file_repo_rel, line=ref.line)}]({url})")
    else:
        out.append("- TODO")
    out.append("")

    out.append("## Metadata")
    out.append("| Key | Value |")
    out.append("| --- | ----- |")
    out.append("| Status | Draft |")
    out.append(f"| Last updated | {today} |")
    out.append("")

    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing entry pages.")
    parser.add_argument(
        "--webkit-root",
        type=Path,
        default=_webkit_root_from_env(),
        help="Path to WebKit checkout (defaults to References/WebKit or WKINTERNALS_WEBKIT_CHECKOUT).",
    )
    args = parser.parse_args()

    if not INDEX_PATH.exists():
        print(f"error: missing symbol index: {INDEX_PATH}", file=sys.stderr)
        return 2

    revision = _read_revision()
    members_index: dict[str, dict[str, list[str]]] = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    decl_index = _build_declaration_index(args.webkit_root)

    written = 0
    skipped = 0
    missing_decl = 0

    for container, categories in members_index.items():
        cocoa_header = _find_cocoa_header_for_container(args.webkit_root, container)
        folder_name = Path(cocoa_header.name).stem if cocoa_header else container
        output_dir = DOCC_COCOA_DIR / folder_name
        output_dir.mkdir(parents=True, exist_ok=True)

        for members in categories.values():
            for member in members:
                filename = _entry_filename_for_member(member)
                out_path = output_dir / filename
                if out_path.exists() and not args.overwrite:
                    skipped += 1
                    continue

                decls = decl_index.get(container, {}).get(member)
                if decls is None or decls.primary() is None:
                    missing_decl += 1

                out_path.write_text(
                    _render_page(container=container, member=member, decls=decls, revision=revision),
                    encoding="utf-8",
                )
                written += 1

    print(f"done: wrote {written}, skipped {skipped}, missing decl {missing_decl}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
