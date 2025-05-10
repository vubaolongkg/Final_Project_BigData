#!/usr/bin/env python3
import sys

current_host = None
current_count = 0

for line in sys.stdin:
    try:
        host, count = line.strip().split('\t')
        count = int(count)

        if current_host == host:
            current_count += count
        else:
            if current_host is not None:
                print(f"{current_host}\t{current_count}")
            current_host = host
            current_count = count
    except:
        continue

# In kết quả cuối cùng
if current_host:
    print(f"{current_host}\t{current_count}")

