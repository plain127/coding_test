# 내가 푼 풀이
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(str, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0

q = deque()
for row in range(n):
    for col in range(n):
        if graph[row][col] == 'T':
            q.append((col, row))

while q:
    x, y = q.popleft()
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and graph[ny][nx] == 'X':
            q.append((nx, ny))
            graph[ny][nx] = 'T'
        elif 0<=nx<n and 0<=ny<n and graph[ny][nx] == 'S':
            count += 1
            graph[ny][nx] = 'T'

if count > 3:
    print('NO')
else:
    print('YES')

#책 풀이
from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))

def watch(x, y, direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1

    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False

def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'
        if not process():
            find = True
            break
        for x, y in data:
            board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')
    