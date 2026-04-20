import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

graph = [list(map(int, input().strip())) for _ in range(9)]
empty = []

has_row = [[False]*10 for _ in range(9)]
has_col = [[False]*10 for _ in range(9)]
has_box = [[False]*10 for _ in range(9)]

def box_idx(r, c):
    return (r // 3) * 3 + (c // 3)

for r in range(9):
    for c in range(9):
        num = graph[r][c]
        if num == 0:
            empty.append((r, c))
        else:
            has_row[r][num] = True
            has_col[c][num] = True
            has_box[box_idx(r, c)][num] = True

def dfs(idx):
    if idx == len(empty):
        for r in range(9):
            print(''.join(map(str, graph[r])))
        sys.exit(0)

    r, c = empty[idx]
    b = box_idx(r, c)

    for num in range(1, 10):
        if not has_row[r][num] and not has_col[c][num] and not has_box[b][num]:
            graph[r][c] = num
            has_row[r][num] = True
            has_col[c][num] = True
            has_box[b][num] = True

            dfs(idx + 1)

            graph[r][c] = 0
            has_row[r][num] = False
            has_col[c][num] = False
            has_box[b][num] = False

dfs(0)