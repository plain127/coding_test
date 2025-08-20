import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dirs = [(-1,0), (0,-1), (0,1), (1,0)]
visited = [[False]*m for _ in range(n)]
answer = 0

def dfs(x, y, depth, total):
    global answer

    if depth == 4:
        answer = max(answer, total)
        return
    
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy

        if 0<=nx<m and 0<=ny<n and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(nx, ny, depth+1, total+board[ny][nx])
            visited[ny][nx] = False


def check_T(x, y):
    global answer

    neighbors = []
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0<=nx<m and 0<=ny<n:
            neighbors.append(board[ny][nx])
    
    if len(neighbors) >= 3:
        s = sum(sorted(neighbors, reverse=True)[:3])+board[y][x]
        if s > answer:
            answer = s

for row in range(n):
    for col in range(m):
        visited[row][col] = True
        dfs(col, row, 1, board[row][col])
        visited[row][col] = False
        check_T(col, row)

print(answer)