import sys

input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

w_cnt = 0
b_cnt = 0

def divide(row, col, size):
    global w_cnt, b_cnt
    color = paper[row][col]
    same = True

    for r in range(row, row+size):
        for c in range(col, col+size):
            if paper[r][c] != color:
                same = False
                break
        if not same:
            break

    if same:
        if color == 0:
            w_cnt+=1
        else:
            b_cnt+=1
    else:
        half = size//2
        divide(row,col,half)
        divide(row+half,col,half)
        divide(row,col+half,half)
        divide(row+half,col+half,half)


divide(0, 0, n)
print(w_cnt)
print(b_cnt)