import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
board = [[0]*n for _ in range(n)]
used = [False]*n
used_up = [False]*(2*(n-1)+1)
used_down = [False]*(2*(n-1)+1)

count = 0

def backtracking(k):
    global n, count

    if k == n:
        count += 1
        return
    
    for i in range(n):
        if not used[i] and not used_up[k+i] and not used_down[(n-1)+k-i]:
            used[i] = True
            used_up[k+i] = True
            used_down[(n-1)+k-i] = True

            backtracking(k+1)

            used[i] = False
            used_up[k+i] = False
            used_down[(n-1)+k-i] = False

backtracking(0)
print(count)