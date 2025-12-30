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

    print(f"Output: {output_dir}")
    if hosting_base_path:
        print(f"Hosting base path: /{hosting_base_path}")
    else:
        print("Hosting base path: /")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
