import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]

if graph[0][1] == 0:
    dp[0][1][0] = 1

for row in range(n):
    for col in range(n):
        if row == 0 and col < 2:
            continue
        if graph[row][col] == 1:
            continue

        if col > 0:
            dp[row][col][0] += dp[row][col-1][0] + dp[row][col-1][2]

        if row > 0:
            dp[row][col][1] += dp[row-1][col][1] + dp[row-1][col][2]

        if row > 0 and col > 0:
            if graph[row][col-1] == 0 and graph[row-1][col] == 0:
                dp[row][col][2] += dp[row-1][col-1][0] + dp[row-1][col-1][1] + dp[row-1][col-1][2]

print(sum(dp[n-1][n-1]))