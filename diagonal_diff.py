#!/usr/bin/env python
n = int(raw_input())
difference = 0
for i in xrange(n):
    row = raw_input().split()
    difference += (int(row[i]) - int(row[n-1-i]))
print abs(difference)
