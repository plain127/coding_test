import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((nx, ny))


t = int(input())
result = []

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for row in range(n):
        for col in range(m):
            if graph[row][col] == 1:
                bfs(col, row)
                count += 1
    
    result.append(count)

for i in result:
    print(i)