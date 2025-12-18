#!/usr/bin/env python3
"""
Generate a DocC member entry page (documentation extension) for a single symbol.

This creates a markdown file under:
  Sources/WKInternalsNotes/Documentation.docc/UIProcess/API/Cocoa/<HeaderStem>/<Entry>.md

Example:
  python3 Scripts/generate_member_page.py WKNavigation/_request

The page includes:
  - Symbol-linked H1 (so DocC renders it as a symbol page)
  - 1-line summary (Japanese placeholder)
  - Objective-C declaration extracted from WebKit sources (best-effort)
  - References with a fixed-revision GitHub link (line anchor when found)
  - Metadata (Status/Last updated)
"""

from __future__ import annotations

import argparse
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


def _strip_outer_backticks(text: str) -> str:
    s = text.strip()
    if s.startswith("``") and s.endswith("``"):
        return s[2:-2].strip()
    return s.strip("`").strip()


def _parse_symbol_ref(arg: str) -> tuple[str, str]:
    s = _strip_outer_backticks(arg)
    if s.startswith(f"{MODULE_NAME}/"):
        s = s[len(f"{MODULE_NAME}/") :]

    parts = s.split("/", 1)
    if len(parts) != 2:
        raise ValueError(f"expected '<Type>/<Member>', got: {arg!r}")
    return parts[0], parts[1]


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
    start_line: int
    body_lines: list[str]


_INTERFACE_RE = re.compile(r"^\s*@interface\s+([A-Za-z_][A-Za-z0-9_]*)\b(.*)$")


def _parse_interface_category(rest: str) -> str | None:
    m = re.match(r"\s*\(\s*([^)]*)\s*\)", rest)
    if not m:
        return None
    return m.group(1)


def _iter_interface_blocks(lines: list[str]) -> Iterable[InterfaceBlock]:
    i = 0
    while i < len(lines):
        line = lines[i]
        m = _INTERFACE_RE.match(line)
        if not m:
            i += 1
            continue

        type_name = m.group(1)
        category = _parse_interface_category(m.group(2))
        start_line = i + 1

        body: list[str] = []
        i += 1
        while i < len(lines):
            if re.match(r"^\s*@end\b", lines[i]):
                break
            body.append(lines[i])
            i += 1
        yield InterfaceBlock(type_name=type_name, category=category, start_line=start_line, body_lines=body)

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
    while i < len(lines):
        stripped = lines[i].lstrip()
        if not stripped.startswith(starters):
            i += 1
            continue

        start_line = base_line + i
        buf: list[str] = [lines[i].rstrip("\n")]
        i += 1
        while i < len(lines) and ";" not in buf[-1]:
            buf.append(lines[i].rstrip("\n"))
            if ";" in lines[i]:
                i += 1
                break
            i += 1
        yield start_line, "\n".join(buf).strip()


@dataclass(frozen=True)
class FoundDecl:
    file_repo_rel: str
    line: int
    decl: str


def _find_member_declaration(
    *,
    webkit_root: Path,
    container: str,
    member: str,
    prefer_files: list[Path],
) -> FoundDecl | None:
    want_property = "(" not in member
    want_method = "(" in member

    # Search preferred files first, then the entire UIProcess tree.
    ui_process_root = webkit_root / WEBKIT_UI_PROCESS_DIR
    candidates: list[Path] = []
    seen: set[Path] = set()
    for p in prefer_files:
        if p.exists() and p not in seen:
            candidates.append(p)
            seen.add(p)
    for p in _iter_files(ui_process_root, exts=(".h", ".m", ".mm")):
        if p not in seen:
            candidates.append(p)
            seen.add(p)

    for path in candidates:
        try:
            raw_lines = path.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
        except Exception:
            continue

        # Protocol members.
        for block in _iter_protocol_blocks(raw_lines):
            if block.name != container:
                continue
            if not block.body_lines:
                continue
            for line_no, decl in _iter_semicolon_decls_with_location(
                block.body_lines,
                starters=("@property", "-", "+"),
                base_line=block.start_line,
            ):
                first = objc._condense_whitespace(decl.splitlines()[0])  # noqa: SLF001
                try:
                    if want_property and first.startswith("@property"):
                        name, _ty = objc._parse_property_symbol(decl)  # noqa: SLF001
                        if name == member:
                            return FoundDecl(file_repo_rel=str(path.relative_to(webkit_root)), line=line_no, decl=decl)
                    if want_method and (first.startswith("-") or first.startswith("+")):
                        sig = objc._parse_method_symbol(decl)  # noqa: SLF001
                        if sig.path_component == member:
                            return FoundDecl(file_repo_rel=str(path.relative_to(webkit_root)), line=line_no, decl=decl)
                except Exception:
                    continue

        # Interface members.
        for block in _iter_interface_blocks(raw_lines):
            if block.type_name != container:
                continue
            for line_no, decl in _iter_semicolon_decls_with_location(
                block.body_lines,
                starters=("@property", "-", "+"),
                base_line=block.start_line,
            ):
                first = objc._condense_whitespace(decl.splitlines()[0])  # noqa: SLF001
                try:
                    if want_property and first.startswith("@property"):
                        name, _ty = objc._parse_property_symbol(decl)  # noqa: SLF001
                        if name == member:
                            return FoundDecl(file_repo_rel=str(path.relative_to(webkit_root)), line=line_no, decl=decl)
                    if want_method and (first.startswith("-") or first.startswith("+")):
                        sig = objc._parse_method_symbol(decl)  # noqa: SLF001
                        if sig.path_component == member:
                            return FoundDecl(file_repo_rel=str(path.relative_to(webkit_root)), line=line_no, decl=decl)
                except Exception:
                    continue

    return None


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
    objc_decl: str | None,
    reference: FoundDecl | None,
    revision: str,
) -> str:
    today = date.today().isoformat()

    out: list[str] = []
    out.append(f"# ``{MODULE_NAME}/{container}/{member}``")
    out.append("")
    out.append("TODO: この API が挙動に与える影響を 1 行で要約する。")
    out.append("")

    out.append("## Objective-C Declaration")
    out.append("```objective-c")
    out.append(objc_decl.strip() if objc_decl else "TODO")
    out.append("```")
    out.append("")

    if "(" not in member:
        out.append("## Default Value")
        out.append("TODO")
        out.append("")

    out.append("## Discussion")
    out.append("TODO: 実装/挙動ベースで説明する（宣言の言い換えで終わらせない）。")
    out.append("")

    out.append("## References")
    if reference is not None:
        url = _github_blob_url(revision, reference.file_repo_rel, line=reference.line)
        out.append(f"- [{_short_link_text(reference.file_repo_rel, line=reference.line)}]({url})")
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
    parser.add_argument("symbol", help="Symbol ref like 'WKNavigation/_request' or 'WKInternalsNotes/WKNavigation/_request'.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite an existing entry page.")
    parser.add_argument(
        "--webkit-root",
        type=Path,
        default=_webkit_root_from_env(),
        help="Path to WebKit checkout (defaults to References/WebKit or WKINTERNALS_WEBKIT_CHECKOUT).",
    )
    args = parser.parse_args()

    container, member = _parse_symbol_ref(args.symbol)
    revision = _read_revision()

    cocoa_header = _find_cocoa_header_for_container(args.webkit_root, container)
    if cocoa_header is None:
        print(
            "error: could not find a Cocoa header for this type.\n"
            f"  - type: {container}\n"
            f"  - searched: {args.webkit_root / WEBKIT_COCOA_HEADERS_DIR}\n"
            "hint: currently this command targets UIProcess/API/Cocoa symbols.",
            file=sys.stderr,
        )
        return 2

    header_stem = cocoa_header.stem  # e.g. WKNavigationPrivate
    out_dir = DOCC_COCOA_DIR / header_stem
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / _entry_filename_for_member(member)

    if out_path.exists() and not args.overwrite:
        print(f"skip: {out_path.relative_to(REPO_ROOT)} (already exists)")
        return 0

    found = _find_member_declaration(
        webkit_root=args.webkit_root,
        container=container,
        member=member,
        prefer_files=[cocoa_header],
    )

    objc_decl = found.decl if found is not None else None
    markdown = _render_page(
        container=container,
        member=member,
        objc_decl=objc_decl,
        reference=found,
        revision=revision,
    )
    out_path.write_text(markdown, encoding="utf-8")
    print(f"wrote: {out_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

