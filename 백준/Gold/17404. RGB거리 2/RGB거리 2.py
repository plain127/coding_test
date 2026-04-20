import sys

input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
dp1 = [[INF]*3 for _ in range(n)]
dp2 = [[INF]*3 for _ in range(n)]
dp3 = [[INF]*3 for _ in range(n)]

dp1[0][0] = cost[0][0]
dp2[0][1] = cost[0][1]
dp3[0][2] = cost[0][2]

for i in range(1, n):
    dp1[i][0] = min(dp1[i-1][1],dp1[i-1][2]) + cost[i][0]
    dp1[i][1] = min(dp1[i-1][0],dp1[i-1][2]) + cost[i][1]
    dp1[i][2] = min(dp1[i-1][0],dp1[i-1][1]) + cost[i][2]

    dp2[i][0] = min(dp2[i-1][1],dp2[i-1][2]) + cost[i][0]
    dp2[i][1] = min(dp2[i-1][0],dp2[i-1][2]) + cost[i][1]
    dp2[i][2] = min(dp2[i-1][0],dp2[i-1][1]) + cost[i][2]

    dp3[i][0] = min(dp3[i-1][1],dp3[i-1][2]) + cost[i][0]
    dp3[i][1] = min(dp3[i-1][0],dp3[i-1][2]) + cost[i][1]
    dp3[i][2] = min(dp3[i-1][0],dp3[i-1][1]) + cost[i][2]

min1 = min(dp1[n-1][1], dp1[n-1][2])
min2 = min(dp2[n-1][0], dp2[n-1][2])
min3 = min(dp3[n-1][0], dp3[n-1][1])

print(min(min1, min2, min3))