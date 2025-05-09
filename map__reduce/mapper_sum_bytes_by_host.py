#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    try:
        fields = next(csv.reader([line]))
        host = fields[0]
        byte = int(fields[6]) if fields[6].isdigit() else 0
        print(f"{host}\t{byte}")
    except:
        continue
