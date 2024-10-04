from collections import deque
#in_file = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = []

graph = [list(map(int, input().strip())) for _ in range(n)]

def bfs(graph, y, x):
    length = len(graph)
    q = deque()
    q.append((x,y))
    graph[y][x] = 0
    count = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= length or ny < 0 or ny >= length:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((nx,ny))
                count += 1
    return count
    
cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)
            