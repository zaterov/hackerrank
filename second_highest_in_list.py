#!/usr/bin/env python

size = int(raw_input())
data = set(map(int, raw_input().split()))
data.remove(max(data))
print(max(data))

