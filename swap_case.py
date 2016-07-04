#!/usr/bin/env python

s = raw_input()
x = []
for i in s:
    if i.isupper():
        x.append(i.lower())
    elif i.islower():
        x.append(i.upper())
    #  else:
        #  x.append(i)

print(''.join(x))
