#!/usr/bin/env python3
import sys

current_type = None
current_count = 0

for line in sys.stdin:
    try:
        resource_type, count = line.strip().split('\t')
        count = int(count)

        if current_type == resource_type:
            current_count += count
        else:
            if current_type is not None:
                print(f"{current_type}\t{current_count}")
            current_type = resource_type
            current_count = count
    except:
        continue

# In loại cuối cùng
if current_type:
    print(f"{current_type}\t{current_count}")
