import sys

input = sys.stdin.readline

original = [list(input().strip()) for _ in range(10)]
answer = 10 ** 9

def toggle(board, row, col):
    dirs = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in dirs:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < 10 and 0 <= nc < 10:
            board[nr][nc] = '#' if board[nr][nc] == 'O' else 'O'


for mask in range(1 << 10):
    board = [row[:] for row in original]
    count = 0

    for col in range(10):
        if mask & (1 << col):
            toggle(board, 0, col)
            count += 1

    for row in range(1, 10):
        for col in range(10):
            if board[row - 1][col] == 'O':
                toggle(board, row, col)
                count += 1

    if all(board[9][col] == '#' for col in range(10)):
        answer = min(answer, count)

if answer == 10 ** 9:
    print(-1)
else:
    print(answer)