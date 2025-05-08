#!/usr/bin/env python3
import sys
for line in sys.stdin:
    if line.startswith("host"):
        continue
    try:
        bytes_sent = int(line.split(",")[6])
        print(f"total\t{bytes_sent}")
    except:
        continue
