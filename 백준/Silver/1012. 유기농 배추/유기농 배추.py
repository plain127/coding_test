import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,0,0,1]
dy = [0,-1,1,0]
total = []

def bfs(x, y):
    q = deque([])
    q.append((x, y))
    graph[y][x] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                q.append((nx, ny))
                graph[ny][nx] = 0

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    count = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                bfs(x, y)
                count += 1
    
    total.append(count)

for i in total:
    print(i)