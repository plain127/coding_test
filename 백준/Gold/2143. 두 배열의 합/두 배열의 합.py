import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

sub_a, sub_b = [], []

for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        sub_a.append(s)

for i in range(m):
    s = 0
    for j in range(i, m):
        s += b[j]
        sub_b.append(s)

sub_b.sort()

ans = 0

for x in sub_a:
    target = t - x
    left = bisect_left(sub_b, target)
    right = bisect_right(sub_b, target)
    ans += right - left

print(ans)