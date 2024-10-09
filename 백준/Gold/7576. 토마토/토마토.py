import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

times = [0]
coord = []
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))    
    
q = deque()

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            q.append((x, y, 0))
    
while q:
    x, y, time = q.popleft()
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        ntime = time + 1
            
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
            graph[ny][nx] = 1
            q.append((nx, ny, ntime))
            times.append(ntime)
            
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            times[-1] = -1
            break

print(times[-1])        