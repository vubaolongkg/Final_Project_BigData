#!/usr/bin/env python3
import sys
import csv

def extract_type(resource):
    parts = resource.strip().split('/')
    if len(parts) > 1 and parts[1]:
        return parts[1].lower()  # lấy phần sau dấu "/" đầu tiên
    return "unknown"

reader = csv.reader(sys.stdin)
header = next(reader)  # bỏ qua header

for row in reader:
    try:
        resource = row[4]  # cột resource
        bytes_sent = row[7]  # cột bytes

        if not resource:
            continue

        resource_type = extract_type(resource)
        bytes_val = int(bytes_sent) if bytes_sent.isdigit() else 0

        print(f"{resource_type}\t{bytes_val}\t1")  # emit: type, bytes, count
    except Exception:
        continue
