#!/usr/bin/env python3
"""Entry program for make.fun the-poster-for-a-place-that-i-2-20261121-0539
(Python 3.13, stdlib only).

Copies the entry image beside this file to /output/entry.png
(or $MAKEFUN_OUTPUT_DIR when set, the kit starter's local-run convention).
Deterministic: the same bytes every run, no network.
"""
import os
import shutil
from pathlib import Path

SRC = Path(__file__).with_name("entry.png")
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT_DIR / "entry.png")
print("wrote", OUT_DIR / "entry.png")
