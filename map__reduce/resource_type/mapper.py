#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    try:
        row = next(csv.reader([line]))
        resource = row[4].strip()  # Cột 'resource'

        if resource.startswith("/"):
            # Lấy phần loại tài nguyên (prefix sau dấu '/')
            parts = resource.split('/')
            if len(parts) > 1 and parts[1]:
                resource_type = parts[1].split('/')[0]
                print(f"{resource_type}\t1")
    except Exception:
        continue
