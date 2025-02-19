#내 풀이
import sys

input = sys.stdin.readline

n = int(input())

soldier = list(map(int, input().split()))
counts = []
for i in range(n-1):
    if soldier[i] < soldier[i+1] :
        counts.append(i)

print(len(counts))

#책 풀이
n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))