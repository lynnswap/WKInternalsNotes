#!/usr/bin/env python3
"""
Update DocC references to link to WebKit on GitHub at a fixed revision.

- Revision source: WebKit.revision (first non-empty, non-comment line)
- GitHub base: https://github.com/WebKit/WebKit
- Resolves line numbers when a local WebKit git checkout is available
  (prefer References/WebKit/; override via WKINTERNALS_WEBKIT_CHECKOUT).
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import generate_webkitspi_private_symbol_graph as gen


REPO_ROOT = Path(__file__).resolve().parents[1]
REVISION_FILE = REPO_ROOT / "WebKit.revision"
DOCC_ROOT = REPO_ROOT / "Sources" / "WKInternalsNotes" / "Documentation.docc"
COCOA_API_ROOT = DOCC_ROOT / "UIProcess" / "API" / "Cocoa"

WEBKIT_GITHUB_BASE = "https://github.com/WebKit/WebKit"
DEFAULT_WEBKIT_CHECKOUT = REPO_ROOT / "References" / "WebKit"


def _read_revision() -> str:
    if not REVISION_FILE.exists():
        raise RuntimeError(f"missing revision file: {REVISION_FILE}")
    for line in REVISION_FILE.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        return s
    raise RuntimeError(f"no revision found in: {REVISION_FILE}")


def _find_webkit_checkout() -> Path | None:
    env = os.environ.get("WKINTERNALS_WEBKIT_CHECKOUT")
    if env:
        p = Path(env).expanduser()
        if (p / ".git").exists():
            return p
    if (DEFAULT_WEBKIT_CHECKOUT / ".git").exists():
        return DEFAULT_WEBKIT_CHECKOUT
    return None


def _git_show(repo: Path, revision: str, path: str) -> str | None:
    try:
        return subprocess.check_output(  # noqa: S603
            ["git", "-C", str(repo), "show", f"{revision}:{path}"],
            stderr=subprocess.DEVNULL,
            text=True,
        )
    except subprocess.CalledProcessError:
        return None


def _github_url(revision: str, path: str, *, line: int | None = None) -> str:
    url = f"{WEBKIT_GITHUB_BASE}/blob/{revision}/{path}"
    if line is not None:
        url += f"#L{line}"
    return url


def _extract_repo_path(line: str) -> str | None:
    m = re.search(r"`(Source/[^`#]+)(?:#L\d+)?`", line)
    return m.group(1) if m else None


def _extract_existing_line_anchor(line: str) -> int | None:
    m = re.search(r"`Source/[^`]+#L(\d+)`", line)
    return int(m.group(1)) if m else None


def _extract_key_hint(line: str) -> str | None:
    m = re.search(r"\(key:\s*`([^`]+)`\)", line)
    return m.group(1) if m else None


def _extract_bullet_suffix(line: str) -> str:
    m = re.match(r"^-\s+(?:\[`Source/[^`]+`\]\([^)]*\)|`Source/[^`]+`)(.*)$", line)
    return m.group(1) if m else ""


def _extract_webpreferences_key(markdown: str) -> str | None:
    m = re.search(r"^\s*-\s*WebPreferences key:\s*`([^`]+)`\s*$", markdown, flags=re.MULTILINE)
    return m.group(1) if m else None


def _line_of_substring(lines: list[str], needle: str) -> int | None:
    for i, line in enumerate(lines, 1):
        if needle in line:
            return i
    return None


def _find_method_decl_line(lines: list[str], labels: list[str]) -> int | None:
    if not labels:
        return None

    if len(labels) == 1:
        name = labels[0]
        rx = re.compile(rf"^[+-]\s*\([^)]*\)\s*{re.escape(name)}\b")
        for i, line in enumerate(lines, 1):
            if rx.search(line):
                return i
        return None

    first = f"{labels[0]}:"
    tail = [f"{l}:" for l in labels[1:]]

    for i, line in enumerate(lines):
        if first not in line:
            continue
        window = "\n".join(lines[i : i + 25])
        if all(t in window for t in tail):
            return i + 1
    return None


@dataclass(frozen=True)
class EntrySymbol:
    kind: str  # property|method|enum|extern|typedef|protocol|interface
    name: str
    method_labels: list[str] | None = None


def _parse_entry_symbol(markdown: str) -> EntrySymbol | None:
    objc_block = gen._extract_first_objc_code_block(markdown)  # noqa: SLF001
    if objc_block is None:
        return None

    first_line = gen._condense_whitespace(objc_block.splitlines()[0])  # noqa: SLF001

    if "typedef NS_ENUM" in objc_block or "typedef NS_OPTIONS" in objc_block:
        enum_name, _cases = gen._parse_enum_symbol(objc_block)  # noqa: SLF001
        return EntrySymbol("enum", enum_name)

    if first_line.startswith("@property"):
        name, _ty = gen._parse_property_symbol(objc_block)  # noqa: SLF001
        return EntrySymbol("property", name)

    if first_line.startswith("-") or first_line.startswith("+"):
        sig = gen._parse_method_symbol(objc_block)  # noqa: SLF001
        objc_labels = [sig.base_name] + [label for (label, _internal, _ty) in sig.params[1:]]
        return EntrySymbol("method", sig.path_component, method_labels=objc_labels)

    if first_line.startswith("@protocol"):
        name = gen._parse_protocol_symbol(objc_block)  # noqa: SLF001
        return EntrySymbol("protocol", name)

    if first_line.startswith("@interface"):
        name = gen._parse_interface_symbol(objc_block)  # noqa: SLF001
        return EntrySymbol("interface", name)

    if first_line.startswith("typedef"):
        name, _ty = gen._parse_typedef_symbol(objc_block)  # noqa: SLF001
        return EntrySymbol("typedef", name)

    if re.match(r"^(extern|FOUNDATION_EXPORT|WK_EXTERN)\b", first_line):
        name, _ty = gen._parse_extern_symbol(objc_block)  # noqa: SLF001
        return EntrySymbol("extern", name)

    return None


def _entry_search_line(repo: Path, revision: str, path: str, entry: EntrySymbol) -> int | None:
    content = _git_show(repo, revision, path)
    if content is None:
        return None
    lines = content.splitlines()

    if entry.kind == "method" and entry.method_labels is not None:
        return _find_method_decl_line(lines, entry.method_labels)

    if entry.kind in {"protocol", "interface"}:
        needle = f"@{entry.kind} {entry.name}"
        return _line_of_substring(lines, needle) or _line_of_substring(lines, entry.name)

    return _line_of_substring(lines, entry.name)


def _yaml_key_line(repo: Path, revision: str, path: str, key: str) -> int | None:
    content = _git_show(repo, revision, path)
    if content is None:
        return None
    lines = content.splitlines()
    rx = re.compile(rf"^\s*{re.escape(key)}\s*:")
    for i, line in enumerate(lines, 1):
        if rx.search(line):
            return i
    return _line_of_substring(lines, key)


def _rewrite_reference_bullet(
    line: str,
    *,
    revision: str,
    repo: Path | None,
    entry: EntrySymbol | None,
    header_path: str | None,
    webpreferences_key: str | None,
) -> str:
    path = _extract_repo_path(line)
    if not path:
        return line

    suffix = _extract_bullet_suffix(line)
    key_hint = _extract_key_hint(suffix)
    existing_anchor_line = _extract_existing_line_anchor(line)
    if key_hint is None and webpreferences_key and path.endswith("UnifiedWebPreferences.yaml"):
        key_hint = webpreferences_key
        if "(key:" not in suffix:
            suffix = f"{suffix} (key: `{key_hint}`)" if suffix else f" (key: `{key_hint}`)"
    anchor_line: int | None = existing_anchor_line

    if repo is not None:
        if key_hint and path.endswith("UnifiedWebPreferences.yaml"):
            anchor_line = _yaml_key_line(repo, revision, path, key_hint)
        elif header_path and path == header_path and entry is not None:
            anchor_line = _entry_search_line(repo, revision, path, entry)
        elif entry is not None:
            anchor_line = _entry_search_line(repo, revision, path, entry)

    link_text = f"`{path}`" if anchor_line is None else f"`{path}#L{anchor_line}`"
    url = _github_url(revision, path, line=anchor_line)

    return f"- [{link_text}]({url}){suffix}"


def _rewrite_implementation_line(
    line: str,
    *,
    revision: str,
    repo: Path | None,
) -> str:
    if "Implementation:" not in line:
        return line

    path = _extract_repo_path(line)
    if not path:
        return line

    existing_anchor_line = _extract_existing_line_anchor(line)
    anchor_line: int | None = None
    if repo is not None:
        content = _git_show(repo, revision, path)
        if content is not None:
            lines = content.splitlines()
            tokens = re.findall(r"`([^`]+)`", line)
            hints = [t for t in tokens if not t.startswith("Source/")]
            needles: list[str] = []
            if hints:
                needles.append(hints[0])
                if "=" in hints[0]:
                    needles.append(hints[0].split("=", 1)[1])
            for needle in needles:
                anchor_line = _line_of_substring(lines, needle)
                if anchor_line is not None:
                    break

    if anchor_line is None:
        anchor_line = existing_anchor_line

    link_text = f"`{path}`" if anchor_line is None else f"`{path}#L{anchor_line}`"
    url = _github_url(revision, path, line=anchor_line)
    replacement = f"[{link_text}]({url})"
    updated, replaced = re.subn(
        rf"\[\[`{re.escape(path)}(?:#L\d+)?`\]\([^)]*\)\]\([^)]*\)",
        replacement,
        line,
        count=1,
    )
    if replaced:
        return updated
    updated, replaced = re.subn(
        rf"\[`{re.escape(path)}(?:#L\d+)?`\]\([^)]*\)",
        replacement,
        line,
        count=1,
    )
    if replaced:
        return updated
    return re.sub(rf"`{re.escape(path)}(?:#L\d+)?`", replacement, line, count=1)


def _update_header_overview_page(markdown: str, *, revision: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    for line in lines:
        if line.startswith("- WebKit revision:"):
            out.append(f"- WebKit revision: [`{revision}`]({WEBKIT_GITHUB_BASE}/tree/{revision})")
            continue
        if line.startswith("- Header (WebKit repo-relative path):"):
            m = re.search(r"`(Source/[^`]+)`", line)
            if not m:
                out.append(line)
                continue
            path = m.group(1)
            url = _github_url(revision, path)
            out.append(f"- Header (WebKit repo-relative path): [`{path}`]({url})")
            continue
        out.append(line)
    return "\n".join(out) + ("\n" if markdown.endswith("\n") else "")


def _update_module_landing_page(markdown: str, *, revision: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    has_baseline = any(line.startswith("- Baseline WebKit revision:") for line in lines)
    for line in lines:
        if line.startswith("- Baseline WebKit revision:"):
            out.append(f"- Baseline WebKit revision: [`{revision}`]({WEBKIT_GITHUB_BASE}/tree/{revision})")
            continue
        out.append(line)
        if not has_baseline and line.strip() == "## Overview":
            out.append(f"- Baseline WebKit revision: [`{revision}`]({WEBKIT_GITHUB_BASE}/tree/{revision})")

    updated = "\n".join(out) + ("\n" if markdown.endswith("\n") else "")
    # If Overview heading doesn't exist, keep original unchanged.
    return updated if "## Overview" in markdown else markdown


def main() -> int:
    revision = _read_revision()
    repo = _find_webkit_checkout()
    if repo is None:
        print(
            "warning: WebKit git checkout not found; links will be updated without line anchors.\n"
            "  - Run: python3 Scripts/bootstrap_webkit_reference.py\n"
            "  - Or set: WKINTERNALS_WEBKIT_CHECKOUT=/path/to/WebKit",
            file=sys.stderr,
        )

    changed = 0

    # Update module landing page.
    landing = DOCC_ROOT / "WKInternalsNotes.md"
    if landing.exists():
        original = landing.read_text(encoding="utf-8")
        updated = _update_module_landing_page(original, revision=revision)
        if updated != original:
            landing.write_text(updated, encoding="utf-8")
            changed += 1

    # Update header overview pages and entry pages.
    for header_page in sorted(COCOA_API_ROOT.glob("*.h.md")):
        original = header_page.read_text(encoding="utf-8")
        updated = _update_header_overview_page(original, revision=revision)
        if updated != original:
            header_page.write_text(updated, encoding="utf-8")
            changed += 1

    containers = gen.discover_header_containers()
    for container, directory in containers.items():
        if not directory.exists():
            continue
        header_path = f"Source/WebKit/UIProcess/API/Cocoa/{container}.h"
        for md_path in sorted(directory.rglob("*.md")):
            original = md_path.read_text(encoding="utf-8")
            entry = _parse_entry_symbol(original)
            lines = original.splitlines()
            out: list[str] = []
            in_references = False
            for line in lines:
                if line.strip() == "## References":
                    in_references = True
                    out.append(line)
                    continue
                if in_references and line.startswith("## "):
                    in_references = False
                if in_references and line.startswith("- "):
                    out.append(
                        _rewrite_reference_bullet(
                            line,
                            revision=revision,
                            repo=repo,
                            entry=entry,
                            header_path=header_path,
                            webpreferences_key=_extract_webpreferences_key(original),
                        )
                    )
                    continue
                if line.startswith("- Implementation:"):
                    out.append(_rewrite_implementation_line(line, revision=revision, repo=repo))
                    continue
                out.append(line)

            updated = "\n".join(out) + ("\n" if original.endswith("\n") else "")
            if updated != original:
                md_path.write_text(updated, encoding="utf-8")
                changed += 1

    print(f"Updated {changed} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
