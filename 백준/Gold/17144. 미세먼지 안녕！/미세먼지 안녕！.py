import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

cleaners = []
for i in range(R):
    if board[i][0] == -1:
        cleaners.append(i)

upper, lower = cleaners[0], cleaners[1]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def spread():
    temp = [[0] * C for _ in range(R)]
    temp[upper][0] = -1
    temp[lower][0] = -1

    for x in range(R):
        for y in range(C):
            if board[x][y] > 0:
                amount = board[x][y] // 5
                cnt = 0

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        temp[nx][ny] += amount
                        cnt += 1

                temp[x][y] += board[x][y] - amount * cnt
    return temp

def operate():
    for i in range(upper - 1, 0, -1):
        board[i][0] = board[i - 1][0]
    for i in range(C - 1):
        board[0][i] = board[0][i + 1]
    for i in range(upper):
        board[i][C - 1] = board[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        board[upper][i] = board[upper][i - 1]
    board[upper][1] = 0

    for i in range(lower + 1, R - 1):
        board[i][0] = board[i + 1][0]
    for i in range(C - 1):
        board[R - 1][i] = board[R - 1][i + 1]
    for i in range(R - 1, lower, -1):
        board[i][C - 1] = board[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        board[lower][i] = board[lower][i - 1]
    board[lower][1] = 0

    board[upper][0] = -1
    board[lower][0] = -1

for _ in range(T):
    board = spread()
    operate()

ans = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            ans += board[i][j]

print(ans)