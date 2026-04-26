import sys
from collections import deque

input = sys.stdin.readline

def value(line, x):
    m, b = line
    return m * x + b

def bad(l1, l2, l3):
    m1, b1 = l1
    m2, b2 = l2
    m3, b3 = l3

    return (b3 - b1) * (m1 - m2) <= (b2 - b1) * (m1 - m3)

n = int(input())

lands = []

for _ in range(n):
    w, h = map(int, input().split())
    lands.append((w, h))
lands.sort()

filtered = []
for w, h in lands:
    while filtered and filtered[-1][1] <= h:
        filtered.pop()
    filtered.append((w, h))

m = len(filtered)
width = [0] + [x[0] for x in filtered]
height = [0] + [x[1] for x in filtered]

dp = [0] * (m + 1)
hull = deque()
hull.append((height[1], dp[0]))

for i in range(1, m + 1):
    x = width[i]

    while len(hull) >= 2 and value(hull[0], x) >= value(hull[1], x):
        hull.popleft()

    dp[i] = value(hull[0], x)

    if i < m:
        new_line = (height[i + 1], dp[i])

        while len(hull) >= 2 and bad(hull[-2], hull[-1], new_line):
            hull.pop()

        hull.append(new_line)

print(dp[m])