import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
count = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    graph[i].sort()

def bfs(start):
    q = deque([])
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()
        
        for leaf in graph[node]:
            if visited[leaf] == False:
                visited[leaf] = True
                q.append(leaf)

for i in range(1,n+1):
    if visited[i] == False:
        bfs(i)
        count+=1

print(count)