import sys

input = sys.stdin.readline

MOD = 1000000007

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

pow2 = [1]*n

for i in range(1,n):
    pow2[i] = (pow2[i-1]*2)%MOD

ans = 0

for i in range(n):
    max_cnt = pow2[i]
    min_cnt = pow2[n-1-i]

    ans += arr[i]*(max_cnt-min_cnt)
    ans %= MOD

print(ans)