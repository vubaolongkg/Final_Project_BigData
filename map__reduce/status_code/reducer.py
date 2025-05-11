#!/usr/bin/env python3
import sys

current_code = None
current_count = 0

for line in sys.stdin:
    try:
        code, count = line.strip().split('\t')
        count = int(count)

        if current_code == code:
            current_count += count
        else:
            if current_code is not None:
                print(f"{current_code}\t{current_count}")
            current_code = code
            current_count = count
    except:
        continue

if current_code:
    print(f"{current_code}\t{current_count}")
