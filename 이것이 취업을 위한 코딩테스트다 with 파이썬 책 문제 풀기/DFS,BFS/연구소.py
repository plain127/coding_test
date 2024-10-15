#내 풀이
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
for y in range(n):
    for x in range(m):
        if graph[y][x] == 2:
            q.append((x,y))
    
while q:
    x, y = q.popleft()
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
            
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
            q.append((nx, ny))

#책 풀이
n, m = map(int, input().split())
data = []
temp = [[0]*m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0-1,1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
                
    return score

def dfs(count):
    global result
    
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
                
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
                    
        result = max(result, get_score())
        return
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
                
dfs(0)
print(result)                        
        
