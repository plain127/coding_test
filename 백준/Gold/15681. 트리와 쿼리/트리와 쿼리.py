import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [0]*(n+1)
visited = [False]*(n+1)

def dfs(root):
    dp[root] = 1
    visited[root] = True

    for nxt in tree[root]:
        if not visited[nxt]:
            dfs(nxt)
            dp[root] += dp[nxt]

dfs(r)

for _ in range(q):
    query = int(input())
    print(dp[query])