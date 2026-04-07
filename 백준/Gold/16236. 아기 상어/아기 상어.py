import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dirs = [(-1,0),(0,-1),(0,1),(1,0)]

s_r, s_c = 0, 0
for row in range(n):
    for col in range(n):
        if graph[row][col] == 9:
            s_r, s_c = row, col
            graph[s_r][s_c] = 0

def bfs(row, col, size):
    visited = [[False]*n for _ in range(n)]
    q = deque([(row, col, 0)])
    visited[row][col] = True
    candidates = []
    m_dist = None

    while q:
        r, c, d = q.popleft()
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and graph[nr][nc] <= size:
                visited[nr][nc] = True
                nd = d + 1
                if 0 < graph[nr][nc] < size:
                    if m_dist is None:
                        m_dist = nd
                    if nd == m_dist:
                        candidates.append((nr, nc))
                else:
                    q.append((nr, nc, nd))

    if not candidates:
        return None

    candidates.sort()
    t_r, t_c = candidates[0]
    return t_r, t_c, m_dist

time = 0
size = 2
eat = 0

while True:
    result = bfs(s_r, s_c, size)
    
    if result == None:
        break

    f_r, f_c, dist = result

    time += dist
    eat += 1
    graph[f_r][f_c] = 0 
    s_r, s_c = f_r, f_c

    if eat == size:
        size+=1
        eat = 0

print(time)