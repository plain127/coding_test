n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(input())

def cell_count(board, n, m):
    count_w = 0  
    count_b = 0  
    w = 'W'
    b = 'B'
    
    for i in range(n, n + 8):
        for j in range(m, m + 8):
            if (i + j) % 2 == 0:
                if board[i][j] != w:
                    count_w += 1
                if board[i][j] != b:
                    count_b += 1
            else:
                if board[i][j] != b:
                    count_w += 1
                if board[i][j] != w:
                    count_b += 1
    
    return min(count_w, count_b)

min_count = []

for i in range(n - 7):
    for j in range(m - 7):
        min_count.append(cell_count(board, i, j))

print(min(min_count))