#내 풀이
from collections import deque

n, k = map(int, input().split())

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

graph = [list(map(int, input().split())) for _ in range(n)]

s, x, y = map(int, input().split())
count = [[0] * n for _ in range(n)]


starts = []
for row in range(n):
    for col in range(n):
        if graph[row][col] != 0:
            virus_type = graph[row][col]
            starts.append((virus_type, row, col))


starts.sort()


q = deque()
for virus, row, col in starts:
    q.append((row, col, 0)) 


while q:
    row, col, time = q.popleft()
    
    if time == s: 
        break
    
    for i in range(4):
        nrow = row + drow[i]
        ncol = col + dcol[i]
    
      
        if 0 <= nrow < n and 0 <= ncol < n and graph[nrow][ncol] == 0:
            graph[nrow][ncol] = graph[row][col] 
            q.append((nrow, ncol, time + 1)) 
    

print(graph[x-1][y-1])

#책 풀이
from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))
            
data.sort()

q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
    virus, s, x, y = q.popleft()
    
    if s == target_s:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))
                
print(graph[target_x - 1 ][target_y - 1])