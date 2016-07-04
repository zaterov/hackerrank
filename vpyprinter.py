#!/usr/bin/env python
from __future__ import print_function

import os

files = []
for f in os.listdir("."):
    if f.endswith(".py"):
        files.append(f)


def sorted_by_time(files):
    mtime = lambda fm: os.stat(fm).st_ctime
    return list((sorted(files, key=mtime)))


lines = []
for f in sorted_by_time(files):
    lines.append(("\n\n{}\n{}".format(f, "-" * len(f))))
    with open(f, 'r') as r:
        for line in r:
            lines.append((line.rstrip()))

print(*lines, sep='\n')

with open('hackerrank-files.txt', 'w') as w:
    w.write('\n'.join(lines))
