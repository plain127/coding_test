import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]

state = [[0]*m for _ in range(n)]
ans =0

def nxt_pos(x, y):
    d = graph[x][y]
    if d == 'U':
        return x-1, y
    elif d == 'D':
        return x+1, y
    elif d == 'L':
        return x, y-1
    else:
        return x, y+1

def dfs(x, y):
    global ans
    state[x][y] = 1

    nx, ny = nxt_pos(x, y)

    if state[nx][ny] == 0:
        dfs(nx, ny)
    elif state[nx][ny] == 1:
        ans += 1
    
    state[x][y] = 2

for r in range(n):
    for c in range(m):
        if state[r][c] == 0:
            dfs(r, c)

print(ans)