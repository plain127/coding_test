import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, n+1):
    graph[i].sort()

visited = [0]*(n+1)
count = 1

def bfs(r):
    q = deque([r])
    global count
    
    visited[r] += count
    count += 1
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] += count
                count += 1

bfs(r)
for i in range(1,n+1):
    print(visited[i])
