import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1,0),(0,-1),(0,1),(1,0)]

def melt():
    visited = [[False]*m for _ in range(n)]
    touched = [[0]*m for _ in range(n)]

    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if 0<=nr<n and 0<=nc<m:
                if not visited[nr][nc] and graph[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))

                if graph[nr][nc] == 1:
                    touched[nr][nc] += 1
    
    cheeze = False
    for row in range(n):
        for col in range(m):
            if touched[row][col] >= 2:
                graph[row][col] = 0
                cheeze = True

    return cheeze

time = 0
melted = True
while melted: 
    melted = melt()
    if melted:
        time += 1

print(time)    