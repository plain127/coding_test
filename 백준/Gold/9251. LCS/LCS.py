import sys

input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

n, m = len(str1), len(str2)

dp = [[0]*(m+1) for _ in range(n+1)]

for row in range(1,n+1):
    s1 = str1[row-1]
    for col in range(1,m+1):
        if str2[col-1] == s1:
            dp[row][col] += dp[row-1][col-1]+1
        else:
            dp[row][col] = max(dp[row][col-1], dp[row-1][col])

print(dp[n][m])