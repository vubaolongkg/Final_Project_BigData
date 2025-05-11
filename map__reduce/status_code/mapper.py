#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    try:
        row = next(csv.reader([line]))
        status_code = row[6].strip()  # Cột 'responsecode'
        if status_code:
            print(f"{status_code}\t1")
    except Exception:
        continue
