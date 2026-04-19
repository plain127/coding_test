import sys

input = sys.stdin.readline

c, n = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
dp = [INF]*(c+101)
dp[0] = 0

for cost, people in cities:
    for i in range(people, c+101):
        dp[i] = min(dp[i], dp[i-people]+cost)

print(min(dp[c:]))