import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(range(1,n+1))
perm = permutations(lst, m)
for p in perm:
    r = map(str, p)
    print(' '.join(r))