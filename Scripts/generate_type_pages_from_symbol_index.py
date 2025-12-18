#!/usr/bin/env python3
"""
Generate DocC type pages from the synthetic symbol index.

This script reads:
  - Sources/WKInternalsNotes/Documentation.docc/SymbolGraphs/WKInternalsNotes.WKAPI.symbols.index.json

and generates documentation extension pages (type pages) that group members by Objective-C category:
  - Sources/WKInternalsNotes/Documentation.docc/UIProcess/API/Cocoa/<HeaderName>.h.md

The output is intentionally minimal: a 1-line summary, Topics grouped by category, and a metadata table.
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

REVISION_FILE = REPO_ROOT / "WebKit.revision"
DOCC_ROOT = REPO_ROOT / "Sources" / "WKInternalsNotes" / "Documentation.docc"
INDEX_PATH = DOCC_ROOT / "SymbolGraphs" / "WKInternalsNotes.WKAPI.symbols.index.json"
OUTPUT_DIR = DOCC_ROOT / "UIProcess" / "API" / "Cocoa"

DEFAULT_WEBKIT_CHECKOUT = REPO_ROOT / "References" / "WebKit"
WEBKIT_COCOA_HEADERS_DIR_REL = Path("Source/WebKit/UIProcess/API/Cocoa")
WEBKIT_HEADER_REPO_REL_DIR = "Source/WebKit/UIProcess/API/Cocoa"

MODULE_NAME = "WKInternalsNotes"


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


def _find_header_for_symbol(symbol: str, *, webkit_headers_dir: Path) -> str | None:
    candidates = [f"{symbol}Private.h", f"{symbol}.h"]
    for name in candidates:
        if (webkit_headers_dir / name).exists():
            return name
    return None


def _category_sort_key(category: str) -> tuple[int, str]:
    priority = {
        "WKPrivate": 0,
        "WKPrivateDeprecated": 1,
        "WKPrivateIOS": 2,
        "WKPrivateMac": 3,
        "WKPrivateVision": 4,
        "WKInternalMac": 5,
        "WKTesting": 10,
        "WKTestingIOS": 11,
        "WKTestingMac": 12,
        "Class Extension": 90,
        "Type": 91,
    }
    return (priority.get(category, 50), category.casefold())


def _format_symbol_link(container: str, member: str) -> str:
    return f"- ``{MODULE_NAME}/{container}/{member}``"


def _render_topics(container: str, categories: dict[str, list[str]]) -> list[str]:
    lines: list[str] = []
    lines.append("## Topics")
    lines.append("")

    for category in sorted(categories.keys(), key=_category_sort_key):
        members = list(categories.get(category, []))
        if not members:
            continue

        properties = [m for m in members if "(" not in m]
        methods = [m for m in members if "(" in m]

        lines.append(f"### {category}")

        if properties and methods:
            lines.append("")
            lines.append("#### Properties")
            lines.extend(_format_symbol_link(container, m) for m in properties)
            lines.append("")
            lines.append("#### Methods")
            lines.extend(_format_symbol_link(container, m) for m in methods)
            lines.append("")
            continue

        lines.append("")
        lines.extend(_format_symbol_link(container, m) for m in (properties or methods))
        lines.append("")

    # Drop trailing blank line if present.
    while lines and lines[-1] == "":
        lines.pop()
    lines.append("")
    return lines


def _render_metadata(*, revision: str, header_name: str | None, today: str) -> list[str]:
    lines: list[str] = [
        "## Metadata",
        "| Key | Value |",
        "| --- | ----- |",
        "| Status | Draft |",
        f"| Last updated | {today} |",
        f"| WebKit revision | [`{revision}`](https://github.com/WebKit/WebKit/tree/{revision}) |",
    ]
    if header_name is not None:
        repo_rel = f"{WEBKIT_HEADER_REPO_REL_DIR}/{header_name}"
        lines.append(
            "| Header (WebKit repo-relative path) | "
            f"[`{header_name}`](https://github.com/WebKit/WebKit/blob/{revision}/{repo_rel}) |"
        )
    return lines + [""]


def _render_page(*, symbol: str, categories: dict[str, list[str]], revision: str, header_name: str | None) -> str:
    today = date.today().isoformat()
    out: list[str] = []
    out.append(f"# ``{MODULE_NAME}/{symbol}``")
    out.append("")
    out.append(f"{symbol} の Objective-C private/testing API をカテゴリ別に整理した一覧。")
    out.append("")
    out.extend(_render_topics(symbol, categories))
    out.extend(_render_metadata(revision=revision, header_name=header_name, today=today))
    return "\n".join(out)


def _symbols_from_private_headers(*, webkit_headers_dir: Path, index: dict[str, dict[str, list[str]]]) -> list[str]:
    symbols: list[str] = []
    for header_path in sorted(webkit_headers_dir.glob("*Private.h")):
        stem = header_path.stem  # e.g. WKWebViewPrivate, _WKInspectorPrivate
        candidates: list[str] = []
        if stem.endswith("Private"):
            candidates.append(stem[: -len("Private")])
        candidates.append(stem)
        for cand in candidates:
            if cand in index:
                symbols.append(cand)
                break
    return sorted(set(symbols), key=str.casefold)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "symbols",
        nargs="*",
        help="Container symbol names to generate (e.g. WKWebView). Omit when using --all-private-headers.",
    )
    parser.add_argument(
        "--all-private-headers",
        action="store_true",
        help="Generate type pages for all *Private.h headers under WebKit UIProcess/API/Cocoa (if present in index).",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files.")
    parser.add_argument(
        "--webkit-root",
        type=Path,
        default=_webkit_root_from_env(),
        help="Path to WebKit checkout (defaults to References/WebKit or WKINTERNALS_WEBKIT_CHECKOUT).",
    )
    args = parser.parse_args()

    revision = _read_revision()
    index: dict[str, dict[str, list[str]]] = json.loads(INDEX_PATH.read_text(encoding="utf-8"))

    webkit_headers_dir = args.webkit_root / WEBKIT_COCOA_HEADERS_DIR_REL
    if not webkit_headers_dir.exists():
        raise RuntimeError(f"missing WebKit Cocoa headers dir: {webkit_headers_dir}")

    symbols = list(args.symbols)
    if args.all_private_headers:
        symbols = _symbols_from_private_headers(webkit_headers_dir=webkit_headers_dir, index=index)

    if not symbols:
        raise RuntimeError("no symbols specified (pass symbols or --all-private-headers)")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    written = 0
    skipped = 0

    for symbol in symbols:
        categories = index.get(symbol)
        if categories is None:
            print(f"warning: missing from index: {symbol}")
            skipped += 1
            continue

        header_name = _find_header_for_symbol(symbol, webkit_headers_dir=webkit_headers_dir)
        output_name = f"{Path(header_name).stem}.h.md" if header_name is not None else f"{symbol}.md"
        out_path = OUTPUT_DIR / output_name

        if out_path.exists() and not args.overwrite:
            print(f"skip: {out_path.relative_to(REPO_ROOT)} (already exists)")
            skipped += 1
            continue

        out_path.write_text(
            _render_page(symbol=symbol, categories=categories, revision=revision, header_name=header_name),
            encoding="utf-8",
        )
        print(f"wrote: {out_path.relative_to(REPO_ROOT)}")
        written += 1

    print(f"done: wrote {written}, skipped {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
