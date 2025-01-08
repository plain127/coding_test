import sys

input = sys.stdin.readline

n = int(input())

triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = [[0]*len(row) for row in triangle]

dp[0][0] = triangle[0][0]

for i in range(1,n):
    for j in range(len(triangle[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == len(triangle[i])-1:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

max_sum = max(dp[-1])

print(max_sum)