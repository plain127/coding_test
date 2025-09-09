import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

parent = [0]*(n+1)
def dfs(node, par):
    for nxt in tree[node]:
        if nxt != par:
            parent[nxt] = node
            dfs(nxt, node)
dfs(1,1)

for i in range(2,n+1):
    print(parent[i])