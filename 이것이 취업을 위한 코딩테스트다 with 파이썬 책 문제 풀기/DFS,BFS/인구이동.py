#내가 푼 풀이
import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

count = 0
def bfs(x, y):
    global count
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        avg = [graph[y][x]]
        row = []
        col = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                d = abs(graph[y][x] - graph[ny][nx])
                if l<=d<=r:
                    q.append((nx,ny))
                    row.append(ny)
                    col.append(nx)
                    avg.append(graph[ny][nx])
        
        if len(avg) > 1:
            count += 1
            h = sum(avg) // len(avg)
            graph[y][x] = h
            for i in range(len(avg)-1):
                kx = col[i]
                ky = row[i]
                graph[ky][kx] = h
    
bfs(0,0)

print(count)

#책 풀이
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(sr, sc, visited):
    """
    (sr, sc)에서 시작하여, 연합에 속하는 모든 칸을 찾아 리스트로 반환합니다.
    또한 연합에 속한 칸들의 인구 합도 함께 반환합니다.
    """
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = True

    union = [(sr, sc)]         # 현재 연합에 속한 칸들(좌표)
    total_population = graph[sr][sc]  # 현재 연합 인구 합

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                # l <= |A[r][c] - A[nr][nc]| <= r 확인
                if l <= abs(graph[r][c] - graph[nr][nc]) <= r:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    union.append((nr, nc))
                    total_population += graph[nr][nc]

    return union, total_population

days = 0

while True:
    visited = [[False]*n for _ in range(n)]
    move_flag = False  # 오늘 하루 인구 이동이 있었는지 확인

    # 모든 칸을 순회하며 BFS로 연합 찾기
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union, total_population = bfs(i, j, visited)
                # 연합에 속한 칸이 2개 이상이라면 인구 이동 수행
                if len(union) > 1:
                    move_flag = True
                    avg = total_population // len(union)
                    # 연합에 속한 칸들을 평균 인구수로 갱신
                    for r, c in union:
                        graph[r][c] = avg

    # 더 이상 연합이 형성되지 않았다면(=인구 이동이 없었다면) 종료
    if not move_flag:
        break
    days += 1

print(days)