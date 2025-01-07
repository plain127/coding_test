import sys

input = sys.stdin.readline

t = int(input())

result = []
for _ in range(t):
    n = int(input())

    dp = [0]*(101)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4,n+1):
        dp[i] = dp[i-2] + dp[i-3]

    result.append(dp[n])

for res in result:
    print(res)  