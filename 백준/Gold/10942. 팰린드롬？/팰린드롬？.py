import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
m = int(input())

dp = [[False]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = True

for i in range(n-1):
    if seq[i] == seq[i+1]:
        dp[i][i+1] = True

for length in range(3, n+1):
    for start in range(n-length+1):
        end = length + start - 1
        if seq[start] == seq[end] and dp[start+1][end-1]:
            dp[start][end] = True

for _ in range(m):
    s, e = map(int, input().split())
    print(1 if dp[s-1][e-1] else 0)