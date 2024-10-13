#내 풀이 == 책 풀이
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
  
visited = [-1]*(n+1)
shortest = [] 
   
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] += 1
    
    while q:
        nx = q.popleft()
        
        if visited[nx] == k:
            shortest.append(nx)
        
        for i in graph[nx]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[nx] + 1

bfs(x)

if len(shortest) == 0:
    print(-1)
else:
    shortest.sort()
    for short in shortest:
        print(short)        
        