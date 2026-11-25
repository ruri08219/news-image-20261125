#!/usr/bin/env python3
"""News-image entry: copy the rendered 25 November 2026 front page to the
output directory, verifying it byte for byte first.

Standard library only. The image itself (entry.png) was drawn locally with
flat vector art and checked by eye: 43 date-checked stories of Wednesday
25 November 2026, 7 regions, 13 drawn illustrations, a numbered world map,
a UTC timeline, a region bar and a date check in the footer.
"""
import hashlib
import os
import pathlib
import shutil
import sys

EXPECTED_SHA256 = "8462f981507915991412272d04040585e210046d7748f5ee07b2aaa7ef8f6e10"
EXPECTED_SIZE = 171041


def main():
    here = pathlib.Path(__file__).resolve().parent
    src = here / "entry.png"
    data = src.read_bytes()
    if len(data) != EXPECTED_SIZE:
        print(f"entry.png size {len(data)} != {EXPECTED_SIZE}", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"entry.png sha256 {digest} != {EXPECTED_SHA256}", file=sys.stderr)
        return 1
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")
    print(f"wrote {out_dir / 'entry.png'} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
