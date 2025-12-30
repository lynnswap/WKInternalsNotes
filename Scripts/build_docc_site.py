#!/usr/bin/env python3
"""
Generate DocC static hosting artifacts for deployment (e.g. GitHub Pages).

Defaults:
- target: WKInternalsNotes
- output dir: docs
- hosting base path: repo name (e.g. WKInternalsNotes)
The output directory is cleaned before generation when it's inside the repo.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGET = "WKInternalsNotes"
DEFAULT_HOSTING_BASE_PATH = REPO_ROOT.name
DEFAULT_OUTPUT_DIR = REPO_ROOT / "docs"
GTM_CONTAINER_ID = "GTM-523NMMLN"


def _run(cmd: list[str], *, cwd: Path | None = None) -> str:
    result = subprocess.run(  # noqa: S603
        cmd,
        cwd=str(cwd) if cwd is not None else None,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"command failed ({result.returncode}): {' '.join(cmd)}\n{result.stdout}")
    return result.stdout.strip()


def _normalize_hosting_base_path(value: str) -> str:
    s = value.strip()
    if s in ("", "/", "."):
        return ""
    return s.strip("/")

def _build_gtm_head_snippet(container_id: str) -> str:
    return (
        "\n    <!-- Google Tag Manager -->\n"
        "    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':\n"
        "    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],\n"
        "    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=\n"
        "    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);\n"
        "    })(window,document,'script','dataLayer','" + container_id + "');</script>\n"
        "    <!-- End Google Tag Manager -->\n"
    )


def _build_gtm_noscript_snippet(container_id: str) -> str:
    return (
        "\n    <!-- Google Tag Manager (noscript) -->\n"
        f'    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id={container_id}"\n'
        '    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>\n'
        "    <!-- End Google Tag Manager (noscript) -->\n"
    )


def _inject_gtm_snippets(html: str, head_snippet: str, noscript_snippet: str) -> tuple[str, bool]:
    updated = html
    changed = False
    if "googletagmanager.com/gtm.js?id=" not in updated:
        marker = "</head>"
        index = updated.rfind(marker)
        if index != -1:
            updated = updated[:index] + head_snippet + updated[index:]
            changed = True
    if "googletagmanager.com/ns.html?id=" not in updated:
        body_match = re.search(r"<body\b[^>]*>", updated, re.IGNORECASE)
        if body_match:
            insert_at = body_match.end()
            updated = updated[:insert_at] + noscript_snippet + updated[insert_at:]
            changed = True
    return updated, changed


def _inject_gtm_into_html_files(output_dir: Path, container_id: str) -> None:
    head_snippet = _build_gtm_head_snippet(container_id)
    noscript_snippet = _build_gtm_noscript_snippet(container_id)
    injected = 0
    for path in output_dir.rglob("*.html"):
        html = path.read_text(encoding="utf-8")
        updated, changed = _inject_gtm_snippets(html, head_snippet, noscript_snippet)
        if changed:
            path.write_text(updated, encoding="utf-8")
            injected += 1
    print(f"GTM injection: {injected} file(s)")


def _write_root_redirect(output_dir: Path) -> None:
    doc_root = output_dir / "documentation"
    if not doc_root.is_dir():
        return

    entries = sorted(p.name for p in doc_root.iterdir() if p.is_dir())
    if len(entries) != 1:
        print("Skip root redirect: expected a single documentation root.")
        return

    target = f"documentation/{entries[0]}/"
    html = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url={target}">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Documentation</title>
  </head>
  <body>
    <p>Redirecting to <a href="{target}">{target}</a>...</p>
  </body>
</html>
"""
    (output_dir / "index.html").write_text(html, encoding="utf-8")
    print(f"Root redirect: / -> {target}")

def _is_within_repo(path: Path) -> bool:
    try:
        path.resolve().relative_to(REPO_ROOT.resolve())
        return True
    except ValueError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate DocC static hosting artifacts.")
    parser.add_argument("--target", default=DEFAULT_TARGET, help="SwiftPM target to document.")
    parser.add_argument(
        "--hosting-base-path",
        default=DEFAULT_HOSTING_BASE_PATH,
        help="Base path for static hosting (GitHub Pages).",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Output directory for static hosting artifacts.",
    )
    args = parser.parse_args()

    hosting_base_path = _normalize_hosting_base_path(args.hosting_base_path)
    output_dir = Path(args.output_dir).expanduser()
    if output_dir.exists():
        if _is_within_repo(output_dir):
            print(f"Cleaning output dir: {output_dir}")
            shutil.rmtree(output_dir)
        else:
            print(f"Warning: output dir is outside repo; skip cleaning: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "swift",
        "package",
        "--allow-writing-to-directory",
        str(output_dir),
        "generate-documentation",
        "--target",
        args.target,
        "--output-path",
        str(output_dir),
        "--transform-for-static-hosting",
    ]
    if hosting_base_path:
        cmd.extend(["--hosting-base-path", hosting_base_path])

    print("Generating DocC documentation...")
    _run(cmd, cwd=REPO_ROOT)

    _write_root_redirect(output_dir)
    _inject_gtm_into_html_files(output_dir, GTM_CONTAINER_ID)

    print(f"Output: {output_dir}")
    if hosting_base_path:
        print(f"Hosting base path: /{hosting_base_path}")
    else:
        print("Hosting base path: /")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
