import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

perm = permutations(nums, m)
for p in perm:
    m = map(str, p)
    print(' '.join(m))