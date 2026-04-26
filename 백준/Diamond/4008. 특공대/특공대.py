import sys
from collections import deque

input = sys.stdin.readline

def value(line, x):
    m, q = line
    return m*x+q

def is_bad(l1,l2,l3):
    m1, q1 = l1
    m2, q2 = l2
    m3, q3 = l3

    return (q1-q2)*(m3-m2) >= (q2-q3)*(m2-m1)

def make_line(index):
    s = prefix[index]
    m = -2*a*s
    q = dp[index] + a*s*s - b*s
    return m, q

n = int(input())
a, b, c = map(int, input().split())

xs = []
while len(xs) < n:
    xs.extend(map(int, input().split()))

prefix = [0]*(n+1)

for i in range(1,n+1):
    prefix[i] = prefix[i-1] + xs[i-1]

dp = [0]*(n+1)

hull = deque()
hull.append(make_line(0))

for i in range(1,n+1):
    x = prefix[i]

    while len(hull) >= 2 and value(hull[0],x) <= value(hull[1], x):
        hull.popleft()

    best = value(hull[0], x)

    dp[i] = a*x*x + b*x + c + best
    new_line = make_line(i)

    while len(hull) >= 2 and is_bad(hull[-2], hull[-1], new_line):
        hull.pop()

    hull.append(new_line)

print(dp[n])