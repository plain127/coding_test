import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[-1]*m for _ in range(n)]
dirs = [(-1,0), (0,-1), (0,1), (1,0)]
visited = [[False]*m for _ in range(n)]

start = None
for row in range(n):
    for col in range(m):
        if graph[row][col] == 2:
            start = (row, col)
        if graph[row][col] == 0:
            result[row][col] = 0
        
q = deque()
q.append((start[0], start[1], 0))
result[start[0]][start[1]] = 0

while q:
    y, x, dist = q.popleft()
    for dy, dx in dirs:
        ny, nx = y+dy, x+dx
        if 0<=ny<n and 0<=nx<m:
            if graph[ny][nx] == 1 and result[ny][nx] == -1:
                result[ny][nx] = dist+1
                q.append((ny, nx, dist+1))

for r in result:
    print(' '.join(map(str, r)))