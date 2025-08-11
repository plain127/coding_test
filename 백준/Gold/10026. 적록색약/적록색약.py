import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
pic = [input().strip() for _ in range(n)]
dx = [-1,0,0,1]
dy = [0,-1,1,0]

def bfs(y, x, col, visit, p):
    q = deque([(x, y, col)])
    while q:
        x, y, col = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and visit[ny][nx] == 0 and p[ny][nx] == col:
                visit[ny][nx] = 1
                q.append((nx, ny, col))

    return 1


n_count = 0
n_visit = [[0]*n for _ in range(n)]
for row in range(n):
    for col in range(n):
        if not n_visit[row][col]:
            n_count += bfs(row, col, pic[row][col], n_visit, pic)

rg_count = 0
rg_visit = [[0]*n for _ in range(n)]
pics = [[]*n for _ in range(n)]
for row in range(n):
    for col in range(n):
        pics[row].append(pic[row][col])
        if pics[row][col] == 'G':
            pics[row][col] = 'R'

for row in range(n):
    for col in range(n):
        if not rg_visit[row][col]:
            rg_count += bfs(row, col, pics[row][col], rg_visit, pics)
print(n_count, rg_count)