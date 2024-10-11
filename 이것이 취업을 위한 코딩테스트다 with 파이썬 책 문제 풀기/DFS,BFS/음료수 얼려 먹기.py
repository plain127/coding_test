#내가 푼 풀이
from collections import deque
n, m = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().strip()))
    
count = 0
def bfs(x, y):
    q = deque()
    q.append((x, y))
    global count
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
                q.append((nx, ny))
                graph[ny][nx] = 1
    
    count += 1            
    
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            bfs(x, y)
            
print(count)

#책 풀이(DFS)
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
    
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)