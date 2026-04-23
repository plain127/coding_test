import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
FULL = (1<<n)-1

dp = [[-1]*(1<<n) for _ in range(n)]

def dfs(cur, visited):
    if visited == FULL:
        if w[cur][0] == 0:
            return INF
        return w[cur][0]

    if dp[cur][visited] != -1:
        return dp[cur][visited]

    dp[cur][visited] = INF

    for nxt in range(n):
        if visited & (1<<nxt):
            continue

        if w[cur][nxt] == 0:
            continue

        cost = w[cur][nxt] + dfs(nxt, visited | (1<<nxt))
        dp[cur][visited] = min(dp[cur][visited], cost)

    return dp[cur][visited]

print(dfs(0, 1<<0))