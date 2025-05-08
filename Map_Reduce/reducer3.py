#!/usr/bin/env python3
import sys
total = 0
for line in sys.stdin:
    _, val = line.strip().split("\t")
    total += int(val)
print(f"Total Bytes:\t{total}")
