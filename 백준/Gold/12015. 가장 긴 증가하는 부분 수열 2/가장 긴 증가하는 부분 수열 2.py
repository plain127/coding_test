import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

lis = []

for x in seq:
    if not lis or lis[-1] < x:
        lis.append(x)
    else:
        idx = bisect_left(lis, x)
        lis[idx] = x

print(len(lis))