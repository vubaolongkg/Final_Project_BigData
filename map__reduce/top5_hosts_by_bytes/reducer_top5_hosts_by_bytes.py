#!/usr/bin/env python3
import sys
from collections import defaultdict

host_bytes = defaultdict(int)

for line in sys.stdin:
    host, val = line.strip().split("\t")
    host_bytes[host] += int(val)

top_hosts = sorted(host_bytes.items(), key=lambda x: x[1], reverse=True)[:5]

for host, total in top_hosts:
    print(f"{host}\t{total}")
