import sys

input = sys.stdin.readline

s = input().strip()
n = len(s)
s = ' '+s

pal = [[False]*(n+1) for _ in range(n+1)]

for length in range(1,n+1):
    for l in range(1, n-length+2):
        r = l+length-1
        if s[l] == s[r] and (length<=2 or pal[l+1][r-1]):
            pal[l][r] = True

INF = int(1e9)
dp = [INF]*(n+1)
dp[0] = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        if pal[j][i]:
            dp[i] = min(dp[i], dp[j-1]+1)

print(dp[n])