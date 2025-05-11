#!/usr/bin/env python3
import sys

max_type = None
max_count = 0

for line in sys.stdin:
    try:
        _, value = line.strip().split('\t')
        resource_type, count = value.split(',')
        count = int(count)

        if count > max_count:
            max_count = count
            max_type = resource_type
    except:
        continue

if max_type:
    print(f"{max_type}\t{max_count}")
