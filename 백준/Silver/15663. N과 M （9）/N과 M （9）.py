import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

perm = permutations(nums, m)
seq = set()

for p in perm:
    seq.add(p)

seq = list(seq)
seq.sort()

for s in seq:
    r = map(str, s)
    print(' '.join(r))