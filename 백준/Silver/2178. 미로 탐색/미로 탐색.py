import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    q = deque([(x, y, 1)])
    graph[y][x] = 0
    
    while q:
        x, y, count = q.popleft()
        
        if x == m -1 and y == n - 1:
            return count
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < m and ny >=0 and ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((nx, ny, count + 1))
    

result = bfs(0, 0)

print(result)  