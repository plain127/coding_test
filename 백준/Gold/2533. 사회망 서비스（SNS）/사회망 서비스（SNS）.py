import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0]*(n+1)
parent[1] = -1

order = []
stack = [1]

while stack:
    u = stack.pop()
    order.append(u)

    for v in graph[u]:
        if v == parent[u]:
            continue

        parent[v] = u
        stack.append(v)

dp0 = [0]*(n+1)
dp1 = [1]*(n+1)

for u in reversed(order):
    for v in graph[u]:
        if parent[v] != u:
            continue

        dp0[u] += dp1[v]

        dp1[u] += min(dp0[v], dp1[v])

print(min(dp0[1], dp1[1]))