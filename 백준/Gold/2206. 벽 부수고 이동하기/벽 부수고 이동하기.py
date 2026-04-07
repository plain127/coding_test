import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dirs = [(-1,0),(0,-1),(0,1),(1,0)]

def bfs(row, col):
    visited = [[[0,0] for _ in range(m)] for _ in range(n)]
    q = deque([(row, col, 0)])
    visited[row][col][0] = 1

    while q:
        r, c, cnt = q.popleft()

        if (r, c) == (n-1, m-1):
            return visited[r][c][cnt]

        for dr, dc in dirs:
            nr, nc = r+dr, c+dc

            if 0<=nr<n and 0<=nc<m:
                if graph[nr][nc] == 1 and cnt == 0 and visited[nr][nc][1] == 0:
                    visited[nr][nc][1] = visited[r][c][cnt] + 1
                    q.append((nr, nc, 1))
                
                if graph[nr][nc] == 0 and visited[nr][nc][cnt] == 0:
                    visited[nr][nc][cnt] = visited[r][c][cnt] + 1
                    q.append((nr, nc, cnt))

    return -1
    
print(bfs(0,0))
