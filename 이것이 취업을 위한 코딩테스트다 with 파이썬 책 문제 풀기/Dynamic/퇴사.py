#내 풀이
import sys

input = sys.stdin.readline

n = int(input())

days = []

for _ in range(n):
    t, p = map(int, input().split())
    days.append((t,p))

dp = [0] * (n+1)

for i in range(n):
    t = days[i][0]
    p = days[i][1]

#책 풀이
n = int(input())
t = []
p = []
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]

    else:
        dp[i] = max_value

print(max_value)