#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    try:
        fields = next(csv.reader([line]))
        response = fields[5]  # Cột status_code
        print(f"{response}\t1")
    except:
        continue
