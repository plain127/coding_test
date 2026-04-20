import sys

input = sys.stdin.readline

seq1 = input().strip()
seq2 = input().strip()

n, m = len(seq1), len(seq2)

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if seq1[i-1] == seq2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])

i, j = n, m
result = []
while i > 0 and j > 0:
    if seq1[i-1] == seq2[j-1]:
        result.append(seq1[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

print(''.join(reversed(result)))