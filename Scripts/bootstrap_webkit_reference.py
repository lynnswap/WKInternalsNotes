#!/usr/bin/env python3
"""
Bootstrap a reference-only WebKit checkout for link/line lookups.

This keeps WebKit out of the build graph and out of git history, while still
allowing tools to resolve line numbers against a fixed revision.

Destination (default): References/WebKit/
Revision source: WebKit.revision (first non-empty, non-comment line)
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REVISION_FILE = REPO_ROOT / "WebKit.revision"
DEFAULT_DEST = REPO_ROOT / "References" / "WebKit"
WEBKIT_REMOTE_URL = "https://github.com/WebKit/WebKit.git"


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


def _read_revision() -> str:
    if not REVISION_FILE.exists():
        raise RuntimeError(f"missing revision file: {REVISION_FILE}")
    for line in REVISION_FILE.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        return s
    raise RuntimeError(f"no revision found in: {REVISION_FILE}")


def main() -> int:
    dest = Path(os.environ.get("WKINTERNALS_WEBKIT_CHECKOUT", str(DEFAULT_DEST))).expanduser()
    revision = _read_revision()

    dest.parent.mkdir(parents=True, exist_ok=True)

    if not (dest / ".git").exists():
        print(f"Cloning WebKit (reference-only) -> {dest.relative_to(REPO_ROOT)}")
        _run(
            [
                "git",
                "clone",
                "--filter=blob:none",
                "--no-checkout",
                WEBKIT_REMOTE_URL,
                str(dest),
            ]
        )
        _run(["git", "-C", str(dest), "sparse-checkout", "init", "--cone"])
        _run(
            [
                "git",
                "-C",
                str(dest),
                "sparse-checkout",
                "set",
                "Source/WebKit/UIProcess",
                "Source/WTF/Scripts/Preferences",
            ]
        )

    print(f"Fetching: {revision}")
    _run(["git", "-C", str(dest), "fetch", "--tags", "origin", revision])
    _run(["git", "-C", str(dest), "checkout", "--detach", revision])
    head = _run(["git", "-C", str(dest), "rev-parse", "HEAD"])
    print(f"Checked out: {revision} ({head})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
