import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
re_graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    re_graph[end].append((start, cost))
    indegree[end] += 1

start, end = map(int, input().split())
dist = [0]*(n+1)

q = deque([start])

while q:
    cur = q.popleft()

    for nxt, cost in graph[cur]:
        candi = dist[cur]+cost

        if dist[nxt] < candi:
            dist[nxt] = candi
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

critical_count = 0
visited = [False]*(n+1)

q = deque([end])
visited[end] = True

while q:
    cur = q.popleft()
    for prev, cost in re_graph[cur]:
        if dist[prev] + cost == dist[cur]:
            critical_count += 1
            if not visited[prev]:
                visited[prev] = True
                q.append(prev)

print(dist[end])
print(critical_count)