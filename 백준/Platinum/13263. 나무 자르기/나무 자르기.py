import sys
from collections import deque

input = sys.stdin.readline


def value(line, x):
    m, c = line
    return m * x + c


def bad(l1, l2, l3):
    m1, c1 = l1
    m2, c2 = l2
    m3, c3 = l3

    return (c2 - c1) * (m2 - m3) >= (c3 - c2) * (m1 - m2)


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * n
hull = deque()

hull.append((b[0], dp[0]))

for i in range(1, n):
    x = a[i]

    while len(hull) >= 2 and value(hull[0], x) >= value(hull[1], x):
        hull.popleft()

    dp[i] = value(hull[0], x)

    new_line = (b[i], dp[i])

    while len(hull) >= 2 and bad(hull[-2], hull[-1], new_line):
        hull.pop()

    hull.append(new_line)

print(dp[n - 1])