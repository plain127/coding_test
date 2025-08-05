import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

def bfs(start):
    q = deque([start])
    visited = [0]*(n+1)
    dist = [0]*(n+1)

    while q:
        idx = q.popleft()
        for d in graph[idx]:
            if not visited[d]:
                dist[d] = dist[idx] + 1
                visited[d] = 1
                q.append(d)

    return  sum(dist)

result = []
for i in range(1, n+1):
    result.append(bfs(i))

min_val = min(result)

print(result.index(min_val)+1)