import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# 거리 배열: -1로 초기화(아직 방문하지 않음을 의미)
distance = [[-1]*m for _ in range(n)]

# 목표지점(2)의 위치 찾기
start_x, start_y = 0, 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            start_x, start_y = i, j
            distance[i][j] = 0  # 자기 자신까지의 거리는 0
            break

# BFS 준비
q = deque()
q.append((start_x, start_y))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 수행
while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 맵 범위 내 + 이동할 수 있는 곳(1) + 아직 방문 안 함(-1)
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == 1 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))

# 결과 출력
# 문제에서 요구하는 대로 0/1/2의 “원래 맵 상태”에 따라 출력 분기
for i in range(n):
    row_result = []
    for j in range(m):
        if maps[i][j] == 0:
            # 원래 갈 수 없는 땅 -> 0 출력
            row_result.append(0)
        else:
            # maps[i][j]가 1 또는 2였던 곳
            # distance가 -1인 경우는 "도달 불가능" -> -1
            row_result.append(distance[i][j] if distance[i][j] != -1 else -1)
    print(' '.join(map(str, row_result)))