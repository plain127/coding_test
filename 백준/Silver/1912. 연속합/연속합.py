import sys

input = sys.stdin.readline

n = int(input())
arrs = list(map(int, input().split()))

dp = [0]*n

dp[0] = arrs[0]

for i in range(1, n):
    dp[i] = max(arrs[i], arrs[i]+dp[i-1])

print(max(dp))