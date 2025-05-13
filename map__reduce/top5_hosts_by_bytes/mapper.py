#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

header = next(reader, None)
if header and header[0] != "host":
    reader = csv.reader([",".join(header)] + list(sys.stdin))

for row in reader:
    try:
        host = row[0]
        bytes_sent = int(row[6]) if row[6] != '-' else 0
        print(f"{host}\t{bytes_sent}")
    except Exception as e:
        continue 
