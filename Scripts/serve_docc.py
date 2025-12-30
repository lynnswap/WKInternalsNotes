#!/usr/bin/env python3
"""
Generate DocC documentation and serve it locally for preview.

Defaults mirror GitHub Pages but use a temporary output directory:
- hosting base path: repo name (e.g. WKInternalsNotes)
- output dir: temporary (deleted on exit)
"""

from __future__ import annotations

import argparse
import subprocess
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGET = "WKInternalsNotes"
DEFAULT_HOSTING_BASE_PATH = REPO_ROOT.name
DEFAULT_PORT = 8000
DEFAULT_PREVIEW_PREFIX = "docc-preview-"


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


def _list_entry_points(output_dir: Path, base_url: str, base_prefix: str) -> None:
    doc_root = output_dir / "documentation"
    tut_root = output_dir / "tutorials"

    if doc_root.is_dir():
        for entry in sorted(p for p in doc_root.iterdir() if p.is_dir()):
            print(f"- {base_url}{base_prefix}/documentation/{entry.name}/")

    if tut_root.is_dir():
        for entry in sorted(p for p in tut_root.iterdir() if p.is_dir()):
            print(f"- {base_url}{base_prefix}/tutorials/{entry.name}/")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate and serve DocC for local preview.")
    parser.add_argument("--target", default=DEFAULT_TARGET, help="SwiftPM target to document.")
    parser.add_argument(
        "--hosting-base-path",
        default=DEFAULT_HOSTING_BASE_PATH,
        help="Base path for static hosting (GitHub Pages).",
    )
    parser.add_argument(
        "--output-dir",
        help="Output directory for static hosting artifacts (kept on exit).",
    )
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Local HTTP port.")
    parser.add_argument("--skip-generate", action="store_true", help="Skip DocC generation.")
    args = parser.parse_args()

    hosting_base_path = _normalize_hosting_base_path(args.hosting_base_path)
    temp_root_context = None
    if args.output_dir:
        output_dir = Path(args.output_dir).expanduser()
    else:
        temp_root_context = tempfile.TemporaryDirectory(prefix=DEFAULT_PREVIEW_PREFIX)
        temp_root = Path(temp_root_context.name)
        output_dir = temp_root / hosting_base_path if hosting_base_path else temp_root
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        if not args.skip_generate:
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

        if hosting_base_path:
            if output_dir.name == hosting_base_path:
                server_root = output_dir.parent
                base_prefix = f"/{hosting_base_path}"
            else:
                server_root = output_dir
                base_prefix = f"/{hosting_base_path}"
                print(
                    "Warning: hosting base path is set, but output-dir name does not match it.\n"
                    "  For preview: use --output-dir <...>/<base-path> or --hosting-base-path /"
                )
        else:
            server_root = output_dir
            base_prefix = ""

        base_url = f"http://localhost:{args.port}"
        print(f"Serving: {server_root}")
        print(f"Base URL: {base_url}{base_prefix}/")
        _list_entry_points(output_dir, base_url, base_prefix)
        if temp_root_context is not None:
            print("Output directory is temporary and will be removed on exit.")
        print("Press Ctrl+C to stop.")

        try:
            result = subprocess.run(  # noqa: S603
                [
                    "python3",
                    "-m",
                    "http.server",
                    str(args.port),
                    "--directory",
                    str(server_root),
                ],
                cwd=str(REPO_ROOT),
                check=False,
            )
        except KeyboardInterrupt:
            return 0
        if result.returncode not in (0, 130):
            raise RuntimeError(f"http.server failed ({result.returncode})")
        return 0
    finally:
        if temp_root_context is not None:
            temp_root_context.cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
