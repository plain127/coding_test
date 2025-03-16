import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()

m = int(input())
targets = list(map(int, input().split()))

def count_by_range(num, target):
    left_idx = bisect_left(num, target)
    right_idx = bisect_right(num, target)
    return right_idx - left_idx

results = []

for target in targets:
    results.append(count_by_range(num, target))

print(' '.join(map(str, results)))