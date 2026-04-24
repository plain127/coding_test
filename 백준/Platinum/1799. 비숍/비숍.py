import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

cells = [[], []]

for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            color = (r+c)%2
            cells[color].append((r,c))

def solve(candi):
    best = 0
    total = len(candi)

    used_sum = [False]*(2*n-1)
    used_diff = [False]*(2*n-1)

    def dfs(idx, cnt):
        nonlocal best

        if cnt+total-idx <= best:
            return

        if idx == total:
            best = max(best, cnt)
            return

        r, c = candi[idx]

        sum_diag = r+c
        diff_diag = r-c+n-1

        if not used_sum[sum_diag] and not used_diff[diff_diag]:
            used_sum[sum_diag] = True
            used_diff[diff_diag] = True

            dfs(idx+1, cnt+1)

            used_sum[sum_diag] = False
            used_diff[diff_diag] = False

        dfs(idx+1, cnt)

    dfs(0,0)
    return best

print(solve(cells[0]) + solve(cells[1]))