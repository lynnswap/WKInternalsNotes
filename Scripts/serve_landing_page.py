#!/usr/bin/env python3
"""
Serve the gh-pages landing page locally for preview.

If a local index.html exists, it is used. Otherwise, this script reads
index.html from a git branch (default: gh-pages) without checkout.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BRANCH = "gh-pages"
DEFAULT_PORT = 8000


def _run_capture(cmd: list[str], *, cwd: Path | None = None) -> str:
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
    return result.stdout


def _read_index_from_git(branch: str, path: str) -> str:
    return _run_capture(["git", "show", f"{branch}:{path}"], cwd=REPO_ROOT)


def _resolve_index_source(branch: str, index_path: Path | None) -> str:
    if index_path is not None:
        return index_path.read_text(encoding="utf-8")

    local_index = REPO_ROOT / "index.html"
    if local_index.exists():
        return local_index.read_text(encoding="utf-8")

    return _read_index_from_git(branch, "index.html")


def main() -> int:
    parser = argparse.ArgumentParser(description="Serve the landing page locally.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Local HTTP port.")
    parser.add_argument("--branch", default=DEFAULT_BRANCH, help="Git branch to read index.html from.")
    parser.add_argument(
        "--index-path",
        type=Path,
        help="Explicit path to index.html (overrides branch lookup).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory for the preview (kept on exit).",
    )
    args = parser.parse_args()

    index_html = _resolve_index_source(args.branch, args.index_path)

    temp_context = None
    if args.output_dir:
        output_dir = args.output_dir.expanduser()
        output_dir.mkdir(parents=True, exist_ok=True)
    else:
        temp_context = tempfile.TemporaryDirectory(prefix="wk-docs-landing-")
        output_dir = Path(temp_context.name)

    (output_dir / "index.html").write_text(index_html, encoding="utf-8")

    print(f"Landing page: http://localhost:{args.port}/")
    if temp_context is not None:
        print("Output directory is temporary and will be removed on exit.")

    result = None
    try:
        result = subprocess.run(  # noqa: S603
            [
                "python3",
                "-m",
                "http.server",
                str(args.port),
                "--directory",
                str(output_dir),
            ],
            cwd=str(REPO_ROOT),
            check=False,
        )
    except KeyboardInterrupt:
        return 0
    finally:
        if temp_context is not None:
            temp_context.cleanup()
    if result is not None and result.returncode not in (0, 130):
        raise RuntimeError(f"http.server failed ({result.returncode})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
