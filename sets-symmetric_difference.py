#!/usr/bin/env python
'''
M = int(raw_input())
S1 = set(map(int, raw_input().split()))
N = int(raw_input())
S2 = set(map(int, raw_input().split()))
'''
M = 4
S1 = {2, 4, 5, 9}
N = 4
S2 = {2, 4, 11, 12}

S = S2.difference(S1)
S.update(S1.difference(S2))
print("\n".join([str(s) for s in (sorted(list(S)))]))
