#내 풀이
import sys

input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(i+1) for i in range(n)]
dp[0][0] = nums[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0 :
            dp[i][j] = dp[i-1][j] + nums[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + nums[i][j]
        else:
            dp[i][j]  = max(dp[i-1][j-1], dp[i-1][j]) + nums[i][j]


result = max(dp[n-1])
print(result)

#책 풀이
n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]
        
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n-1]))