#!/usr/bin/env python3
import sys

current_type = None
total_bytes = 0
total_count = 0

for line in sys.stdin:
    try:
        resource_type, bytes_val, count = line.strip().split("\t")
        bytes_val = int(bytes_val)
        count = int(count)

        if current_type != resource_type:
            if current_type:
                avg = total_bytes / total_count if total_count else 0
                print(f"{current_type}\t{avg:.2f}")
            current_type = resource_type
            total_bytes = bytes_val
            total_count = count
        else:
            total_bytes += bytes_val
            total_count += count
    except:
        continue

# In kết quả cuối cùng
if current_type:
    avg = total_bytes / total_count if total_count else 0
    print(f"{current_type}\t{avg:.2f}")
