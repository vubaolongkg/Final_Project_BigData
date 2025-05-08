#!/usr/bin/env python3
import sys
for line in sys.stdin:
    if line.startswith("host") or line.strip() == "":
        continue
    parts = line.split(",")
    print(f"{parts[0]}\t1")