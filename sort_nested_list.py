#!/usr/bin/env python

size = int(raw_input())

l = []
if 2 <= size <= 5:
    for i in range(size):
        name = raw_input()
        grade = int(raw_input())
        l.append([name, grade])


G = sorted(l, key=lambda x: int(x[1]))
G = G[1:]

grade = G[0][1]

names = [[0] for x in G if x[1] == grade]

print('\n'.join([str(s) for s in sorted(names)]))


'''
data = set(map(int, raw_input().split()))
data.remove(max(data))
print(max(data))
'''

