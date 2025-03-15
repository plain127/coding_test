import sys

input = sys.stdin.readline

def fibonacci(n,dp):
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for i in range(2, n+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

results = []
for _ in range(int(input())):
    n = int(input())
    dp = [[0,0] for _ in range(41)]

    fibonacci(n, dp)
    results.append(dp[n])

for result in results:
    zero, one = result
    print(zero, one)