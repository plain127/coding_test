import sys

input = sys.stdin.readline

n, k = map(int, input().split())
line = list(map(int, input().split()))

p_sum = [0]*(n+1)
for i in range(1, n+1):
    p_sum[i] = p_sum[i-1] + line[i-1]

m = -10**9
for i in range(k, n+1):
    r = p_sum[i] - p_sum[i-k]
    m = max(m, r)
print(m)