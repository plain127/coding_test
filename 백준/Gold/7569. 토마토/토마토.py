import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

times = [0]
graph = [[[] for _ in range(n)] for _ in range(h)]

for z in range(h):
    for y in range(n):
        graph[z][y] = list(map(int, input().split()))    
    
q = deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                q.append((x, y, z, 0))
    
while q:
    x, y, z, time = q.popleft()
        
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        ntime = time + 1
            
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and graph[nz][ny][nx] == 0:
            graph[nz][ny][nx] = 1
            q.append((nx, ny, nz, ntime))
            times.append(ntime)

for z in range(h):            
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 0:
                times[-1] = -1
                break

print(times[-1])      