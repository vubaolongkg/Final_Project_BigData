#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    try:
        fields = next(csv.reader([line]))
        hour = fields[11]  # Cột ts_hour
        print(f"{hour}\t1")
    except:
        continue
