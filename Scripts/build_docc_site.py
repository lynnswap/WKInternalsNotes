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
import shutil
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGET = "WKInternalsNotes"
DEFAULT_HOSTING_BASE_PATH = REPO_ROOT.name
DEFAULT_OUTPUT_DIR = REPO_ROOT / "docs"
GA4_MEASUREMENT_ID = "G-S77B1SXVCF"


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

def _build_ga4_snippet(measurement_id: str) -> str:
    return (
        "\n    <!-- Google tag (gtag.js) -->\n"
        f'    <script async src="https://www.googletagmanager.com/gtag/js?id={measurement_id}"></script>\n'
        "    <script>\n"
        "      window.dataLayer = window.dataLayer || [];\n"
        "      function gtag(){dataLayer.push(arguments);}\n"
        "      gtag('js', new Date());\n"
        "\n"
        f"      gtag('config', '{measurement_id}');\n"
        "    </script>\n"
    )


def _inject_ga4_snippet(html: str, snippet: str) -> tuple[str, bool]:
    if "googletagmanager.com/gtag/js?id=" in html:
        return html, False
    marker = "</head>"
    index = html.rfind(marker)
    if index == -1:
        return html, False
    return html[:index] + snippet + html[index:], True


def _inject_ga4_into_html_files(output_dir: Path, measurement_id: str) -> None:
    snippet = _build_ga4_snippet(measurement_id)
    injected = 0
    for path in output_dir.rglob("*.html"):
        html = path.read_text(encoding="utf-8")
        updated, changed = _inject_ga4_snippet(html, snippet)
        if changed:
            path.write_text(updated, encoding="utf-8")
            injected += 1
    print(f"GA4 injection: {injected} file(s)")


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
    _inject_ga4_into_html_files(output_dir, GA4_MEASUREMENT_ID)

    print(f"Output: {output_dir}")
    if hosting_base_path:
        print(f"Hosting base path: /{hosting_base_path}")
    else:
        print("Hosting base path: /")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
