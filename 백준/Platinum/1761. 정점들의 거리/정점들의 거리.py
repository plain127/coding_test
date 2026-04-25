import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, distance = map(int, input().split())
    graph[a].append((b, distance))
    graph[b].append((a, distance))

LOG = (N).bit_length()

parent = [[0] * (N + 1) for _ in range(LOG)]

depth = [-1] * (N + 1)

dist_from_root = [0] * (N + 1)

queue = deque([1])

depth[1] = 0

while queue:
    current = queue.popleft()

    for next_node, edge_distance in graph[current]:
        if depth[next_node] != -1:
            continue

        parent[0][next_node] = current

        depth[next_node] = depth[current] + 1

        dist_from_root[next_node] = dist_from_root[current] + edge_distance

        queue.append(next_node)


for k in range(1, LOG):
    for node in range(1, N + 1):
        half_ancestor = parent[k - 1][node]
        parent[k][node] = parent[k - 1][half_ancestor]

def find_lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
    for k in range(LOG):
        if diff & (1 << k):
            a = parent[k][a]

    if a == b:
        return a
    for k in range(LOG - 1, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    return parent[0][a]

M = int(input())

answer = []

for _ in range(M):
    a, b = map(int, input().split())

    common = find_lca(a, b)

    distance = (
        dist_from_root[a]
        + dist_from_root[b]
        - 2 * dist_from_root[common]
    )

    answer.append(str(distance))

print("\n".join(answer))