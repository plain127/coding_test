import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def merge(line):
    arr = [x for x in line if x != 0]
    res = []
    i = 0

    while i < len(arr):
        if i + 1 < len(arr) and arr[i] == arr[i + 1]:
            res.append(arr[i] * 2)
            i += 2
        else:
            res.append(arr[i])
            i += 1

    res += [0] * (n - len(res))
    return res

def move(b, d):
    nb = [[0] * n for _ in range(n)]

    if d == 0:
        for r in range(n):
            nb[r] = merge(b[r])

    elif d == 1:
        for r in range(n):
            nb[r] = merge(b[r][::-1])[::-1]

    elif d == 2:
        for c in range(n):
            line = [b[r][c] for r in range(n)]
            merged = merge(line)
            for r in range(n):
                nb[r][c] = merged[r]

    else:  
        for c in range(n):
            line = [b[r][c] for r in range(n)][::-1]
            merged = merge(line)[::-1]
            for r in range(n):
                nb[r][c] = merged[r]

    return nb

def dfs(depth, b):
    global ans

    for r in range(n):
        ans = max(ans, max(b[r]))

    if depth == 5:
        return

    for d in range(4):
        nb = move(b, d)
        dfs(depth + 1, nb)

dfs(0, board)
print(ans)