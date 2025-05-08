#!/usr/bin/env python3
import sys
for line in sys.stdin:
    if line.startswith("code") or line.strip() == "":
        continue
    parts = line.split(",")
    print(f"{parts[6]}\t1")