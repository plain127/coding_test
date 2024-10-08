import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
dxs = [-2,-2,-1,-1,1,1,2,2]
dys = [-1,1,-2,2,-2,2,-1,1]

def bfs(x_c, y_c, x_d, y_d):
    q = deque()
    q.append((x_c, y_c))
    visited[y_c][x_c] = 0

    while q:
        x, y = q.popleft()

        if x == x_d and y == y_d:
            break
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < l and 0 <= ny < l and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((nx, ny))

results = []
for _ in range(t):
    l = int(input())
    visited = [[-1]*(l+1) for _ in range(l+1)]
    x_c, y_c = map(int, input().split())
    x_d, y_d = map(int, input().split())
    bfs(x_c, y_c, x_d, y_d)
    results.append(visited[y_d][x_d])

for result in results:
    print(result)