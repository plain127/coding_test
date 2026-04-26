import sys

input = sys.stdin.readline

MAX_POINT = 100

n = int(input())
pair = [0]*(MAX_POINT+2)

for _ in range(n):
    a, b = map(int, input().split())
    pair[a] = b
    pair[b] = a

dp = [[0]*(MAX_POINT+2) for _ in range(MAX_POINT+2)]

for length in range(1, MAX_POINT+1):
    for start in range(1, MAX_POINT-length+2):
        end = start + length - 1

        dp[start][end] = dp[start+1][end]

        other = pair[start]

        if start < other <= end:
            selected = dp[start+1][other-1] + dp[other+1][end] + 1
            dp[start][end] = max(dp[start][end], selected)

print(dp[1][MAX_POINT])