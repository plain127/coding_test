import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

def bfs(x_c, y_c):
    q = deque()
    q.append((x_c, y_c))
    visited[y_c][x_c] += 1
    
    while q:
        x_c, y_c = q.popleft()
        
        if x_c == x_d and y_c == y_d:
            return visited[y_c][x_c]
        
        for x, y in zip(dx, dy):
            nx = x_c + x
            ny = y_c + y
            if 0 <= nx < l and 0 <= ny < l and visited[ny][nx] == -1:
                q.append((nx, ny))
                visited[ny][nx] = visited[y_c][x_c] + 1

results = []
      
for _ in range(t):
    l = int(input())
    visited = [[-1]*(l) for _ in range(l)]
    
    x_c, y_c = map(int, input().split())
    x_d, y_d = map(int, input().split())
    
    results.append(bfs(x_c, y_c))

for result in results:
    print(result)