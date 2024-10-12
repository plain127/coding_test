#내 풀이
from collections import deque

n, m = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().strip()))

def bfs(x, y, count):
    q = deque()
    q.append((x, y, count))
    graph[y][x] = 0
    
    while q:
        x, y, count = q.popleft()
    
        
        if x == m-1 and y == n-1:
            return count
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((nx, ny, count + 1))
    

print(bfs(0, 0, 1))

#책 풀이
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n-1][m-1]

print(bfs(0,0))