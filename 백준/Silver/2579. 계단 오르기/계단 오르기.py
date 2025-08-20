import sys

input = sys.stdin.readline

n = int(input())
score = [0] + [int(input()) for _ in range(n)]
dp = [0]

for i in range(1, n+1):
    if i == 1:
        dp.append(score[i])
    elif i == 2:
        dp.append(dp[i-1]+score[i])
    else:
        dp.append(max(dp[i-2], dp[i-3]+score[i-1])+score[i])

print(dp[n])