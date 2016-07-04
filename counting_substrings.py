#!/usr/bin/env python

s, pattern = [raw_input() for _ in range(2)]
cnt = 0
for i in range(len(s)):
    if s[i:i+len(pattern)] == pattern:
        cnt += 1 
print(cnt)
