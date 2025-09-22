import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


def dfs(start, dis, visited):
    visited[start] = True
    far_node, far_dis = start, dis

    for v, w in graph[start]:
        if not visited[v]:
            node, di = dfs(v, dis+w, visited)
            if di > far_dis:
                far_node, far_dis = node, di

    return far_node, far_dis

visited = [False]*(n+1)
node, _ = dfs(1, 0, visited)

visited = [False]*(n+1)
_, ans = dfs(node, 0, visited)
print(ans)