#내 풀이
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    golds = [[] for _ in range(n)]

    q = deque(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            golds[i].append(q[j])
        
        for _ in range(m):
            q.popleft()

    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        dp[i][0] = golds[i][0]

    for i in range(n):
        for j in range(1, m):
            if i == 0:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1]) + golds[i][j]
            elif i == n :
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1]) + golds[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + golds[i][j]

    result = max(dp[n])

    print(result)

#책 풀이
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index+=m
    
    for j in range(1,m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
        
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)