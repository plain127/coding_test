import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]


dx = [-1,0,0,1]
dy = [0,-1,1,0]

def bfs(x, y):
    q = deque([])
    q.append((x, y, 0))
    visited[y][x][0] = 1

    while q:
        x, y, count = q.popleft()

        if (x, y) == (m-1, n-1):
            return visited[y][x][count]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if map[ny][nx] == 1 and count == 0 and visited[ny][nx][1] == 0:
                    visited[ny][nx][1] = visited[y][x][count] + 1
                    q.append((nx, ny, 1))
                
                if map[ny][nx] == 0 and visited[ny][nx][count] == 0:
                    visited[ny][nx][count] = visited[y][x][count] + 1
                    q.append((nx, ny, count))

    return -1

print(bfs(0, 0))