#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        resource_type, count = line.strip().split('\t')
        print(f"max\t{resource_type},{count}")
    except:
        continue
