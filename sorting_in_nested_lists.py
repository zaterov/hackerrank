#!/usr/bin/env python

size = int(raw_input())

l = []
grades = []
if 2 <= size <= 5:
    for _ in range(size):
        name = raw_input()
        grade = float(raw_input())
        l.append([name, grade])
        grades.append(grade)

grade = sorted(list(set(grades)))[1]
names = [x[0] for x in l if x[1] == grade]
print('\n'.join([str(s) for s in sorted(names)]))


'''
data = set(map(float, raw_input().split()))
data.remove(max(data))
prfloat(max(data))
'''

