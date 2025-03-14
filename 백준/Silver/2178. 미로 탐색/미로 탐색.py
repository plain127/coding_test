import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dx = [-1,0,0,1]
dy = [0,-1,1,0]

q = deque([])
q.append((0,0,1))
graph[0][0] = 0

result = 0

while q:
    x, y, count = q.popleft()
    
    if x == m-1 and y == n-1:
        result = count

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
            q.append((nx, ny, count+1))
            graph[ny][nx] = 0

print(result)