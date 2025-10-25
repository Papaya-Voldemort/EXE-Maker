#!/usr/bin/env python3
import shutil
import os

src = "/Volumes/External Home/Kids Home/PycharmProjects/Tkinter/tomato.png"
dst = "/Volumes/External Home/Kids Home/PycharmProjects/Tkinter/exe_versions/tomato.png"

if os.path.exists(src):
    shutil.copy2(src, dst)
    print(f"✓ Copied tomato.png to exe_versions/")
else:
    print(f"✗ Source file not found: {src}")

