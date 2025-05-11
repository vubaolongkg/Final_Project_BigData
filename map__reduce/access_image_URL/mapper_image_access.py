#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    try:
        row = next(csv.reader([line]))

        host = row[0].strip()
        resource = row[4].strip()  # Cột 'resource'

        if resource.startswith("/image"):
            print(f"{host}\t1")
    except Exception:
        continue  # Bỏ qua dòng lỗi

