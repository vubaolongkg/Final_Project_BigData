#!/usr/bin/env python3
import sys
from collections import defaultdict

counts = defaultdict(int)
for line in sys.stdin:
    code, count = line.strip().split("\t")
    counts[code] += int(count)
for code, total in counts.items():
    print(f"{code}\t{total}")
