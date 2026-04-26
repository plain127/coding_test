import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

log = n.bit_length()

parent = [[0] * (n + 1) for _ in range(log)]
depth = [-1] * (n + 1)

queue = deque([1])
depth[1] = 0

while queue:
    node = queue.popleft()

    for next_node in graph[node]:
        if depth[next_node] != -1:
            continue

        depth[next_node] = depth[node] + 1
        parent[0][next_node] = node
        queue.append(next_node)

for k in range(1, log):
    for node in range(1, n + 1):
        mid_parent = parent[k - 1][node]
        parent[k][node] = parent[k - 1][mid_parent]


def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]

    for k in range(log):
        if diff & (1 << k):
            a = parent[k][a]

    if a == b:
        return a

    for k in range(log - 1, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    return parent[0][a]


m = int(input())
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    answer.append(str(lca(a, b)))

print('\n'.join(answer))