#!/usr/bin/env python3
import sys
from collections import defaultdict

counts = defaultdict(int)
for line in sys.stdin:
    host, count = line.strip().split("\t")
    counts[host] += int(count)
for host, total in counts.items():
    print(f"{host}\t{total}")
