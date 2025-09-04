import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]

for row in range(1, n+1):
    for col in range(1, n+1):
        dp[row][col] = graph[row-1][col-1] + dp[row-1][col] + dp[row][col-1] - dp[row-1][col-1]

results = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    results.append(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])

for r in results:
    print(r)