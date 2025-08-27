import sys

input = sys.stdin.readline

result = []
for _ in range(int(input())):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]

    dp[0][0], dp[1][0] = score[0][0], score[1][0]

    if n > 1:
        dp[0][1], dp[1][1] = dp[1][0]+score[0][1], dp[0][0]+score[1][1]

    for col in range(2, n):
        dp[0][col] = max(dp[0][col-2], dp[1][col-1], dp[1][col-2]) + score[0][col]
        dp[1][col] = max(dp[0][col-1], dp[0][col-2], dp[1][col-2]) + score[1][col]

    result.append(max(dp[0][n-1], dp[1][n-1]))

for r in result:
    print(r)