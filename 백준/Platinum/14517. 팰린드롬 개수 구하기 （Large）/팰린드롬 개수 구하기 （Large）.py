import sys

input = sys.stdin.readline

MOD = 10007

s = input().strip()
n = len(s)
dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for length in range(2, n+1):
    for left in range(n-length+1):
        right = left + length - 1

        without_left = dp[left+1][right]
        without_right = dp[left][right-1]
        dp[left][right] = without_left + without_right

        duplicated = dp[left+1][right-1]
        dp[left][right] -= duplicated

        if s[left] == s[right]:
            pair_only = 1
            inside = dp[left+1][right-1]
            dp[left][right] += inside + pair_only
        
        dp[left][right] %= MOD

print(dp[0][n-1])