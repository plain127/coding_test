import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = list(range(101))

for _ in range(n):
    x, y = map(int, input().split())
    board[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    board[u] = v

moves = [-1]*101
moves[1] = 0
q = deque([1])

while q:
    cur = q.popleft()
    if cur == 100:
        break
    for dice in range(1,7):
        next = cur + dice
        if next > 100 :
            continue

        next = board[next]
        if moves[next] == -1:
            moves[next] = moves[cur] + 1
            q.append(next)

print(moves[100])