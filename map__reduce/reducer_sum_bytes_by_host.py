#!/usr/bin/env python3
import sys

current_host = None
total = 0

for line in sys.stdin:
    host, val = line.strip().split("\t")
    val = int(val)
    if host == current_host:
        total += val
    else:
        if current_host:
            print(f"{current_host}\t{total}")
        current_host = host
        total = val

if current_host:
    print(f"{current_host}\t{total}")
