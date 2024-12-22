import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    q = deque()
    q.append([x, y, 1])
    graph[y][x] = 0
    
    while q :
        x, y, count = q.popleft()

        if x == m-1 and y == n-1:
            return count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append([nx, ny, count+1])

result = bfs(0,0)

print(result)