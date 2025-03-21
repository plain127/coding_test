import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(str, input().strip())))

dx = [1,0,-1,0]
dy = [0,1,-0,-1]

def bfs(x, y):
    q = deque([])
    q.append((x,y))
    count = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] != 'X':
                if graph[ny][nx] == 'P':
                    count += 1
                
                graph[ny][nx] = 'X'
                q.append((nx, ny))

    return count

result = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 'I':
            result += bfs(x, y)

if result == 0:
    print('TT')
else:
    print(result)