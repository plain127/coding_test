from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y, m, n):
    q = deque()
    q.append((x, y))
    graph[y][x] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((nx, ny))
                

t = int(input())
cnt = []
for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                bfs(graph, x, y, m, n)
                count += 1
    cnt.append(count)

for i in cnt:
    print(i)