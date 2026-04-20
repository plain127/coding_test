import sys

input = sys.stdin.readline

cmd = list(map(int, input().split()))
cmd.pop()

INF = int(1e9)

def move(a, b):
    if a == b:
        return 1
    if a == 0:
        return 2
    if abs(a-b) == 2:
        return 4
    return 3

n = len(cmd)
dp = [[[INF]*5 for _ in range(5)] for _ in range(n+1)]
dp[0][0][0] = 0

for i in range(n):
    x = cmd[i]
    for l in range(5):
        for r in range(5):
            if dp[i][l][r] == INF:
                continue

            dp[i+1][x][r] = min(dp[i+1][x][r], dp[i][l][r]+move(l,x))
            dp[i+1][l][x] = min(dp[i+1][l][x], dp[i][l][r]+move(r,x))

ans = INF
for l in range(5):
    for r in range(5):
        ans = min(ans, dp[n][l][r])

print(ans)