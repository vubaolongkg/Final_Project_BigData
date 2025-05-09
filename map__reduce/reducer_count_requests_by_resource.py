#!/usr/bin/env python3
import sys

current_code = None
count = 0

for line in sys.stdin:
    code, val = line.strip().split("\t")
    val = int(val)
    if code == current_code:
        count += val
    else:
        if current_code:
            print(f"{current_code}\t{count}")
        current_code = code
        count = val

if current_code:
    print(f"{current_code}\t{count}")
