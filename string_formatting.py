#!/usr/bin/env python

N = int(raw_input())

if 1 <= N <= 99:
    width = len('{0:b}'.format(N))

    for i in xrange(1, N + 1):
        print '{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=width)

'''
the instructions neglect to say that the hex must be uppercase
'''
