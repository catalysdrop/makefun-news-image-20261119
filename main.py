#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261119 (Python 3.13, stdlib only).

Writes the front-page image for Thursday 19 November 2026 to the
output directory the grader provides. The image was composed in this
very session: five scenes from that day - GTA VI rolling out in Vice
City, the Trump-Xi-Putin handshake at APEC in Shenzhen, the Israeli
ground raid across the Gaza ceasefire line, the new attack on the
Crimea bridge, and Anthropic's record IPO - arranged as a newspaper
front page with a masthead naming the day, numbered caption bars and
a footer line. The program only copies bytes, so both graded runs
write exactly the same file.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().with_name("entry.png")


def sha256(path: Path) -> str:
    """Hash of a file's bytes, used to prove the copy is exact."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    if sha256(target) != sha256(SOURCE):
        print("entry.png differs after copy", file=sys.stderr)
        return 1
    print(f"wrote {target} ({target.stat().st_size} bytes, sha256 {sha256(target)[:12]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
