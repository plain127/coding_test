import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1,0), (0,-1), (0,1), (1,0)]

virus = []
walls = []
total = 0
for row in range(n):
    for col in range(m):
        if graph[row][col] == 2:
            virus.append((row, col))
        elif graph[row][col] == 0:
            walls.append((row, col))
            total+=1

c = list(combinations(walls, 3))

def bfs(a, b, c):
    count = total-3
    visited = [[False]*m for _ in range(n)]
    q = deque([])

    for v in virus:
        r, c = v
        visited[r][c] = True
        q.append((r, c))
    
    while q:
        y, x = q.popleft()

        for dy, dx in dirs:
            ny, nx = y+dy, x+dx

            if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and graph[ny][nx] == 0:
                visited[ny][nx] = True
                q.append((ny, nx))
                count-=1
    
    return count
    

cnt = 0
for a, b, c in c:
    graph[a[0]][a[1]] = 1
    graph[b[0]][b[1]] = 1
    graph[c[0]][c[1]] = 1
    cnt = max(cnt, bfs(a, b, c))
    graph[a[0]][a[1]] = 0
    graph[b[0]][b[1]] = 0
    graph[c[0]][c[1]] = 0

print(cnt)