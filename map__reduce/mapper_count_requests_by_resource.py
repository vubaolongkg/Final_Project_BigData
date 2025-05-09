#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    try:
        fields = next(csv.reader([line]))
        resource = fields[4]
        print(f"{resource}\t1")
    except:
        continue
