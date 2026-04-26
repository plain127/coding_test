import sys

input = sys.stdin.readline

MOD = 1000000007
MAX = 4000000

fact = [1]*(MAX+1)

for i in range(1, MAX+1):
    fact[i] = fact[i-1]*i%MOD

inv_fact = [1]*(MAX+1)
inv_fact[MAX] = pow(fact[MAX], MOD-2, MOD)

for i in range(MAX, 0, -1):
    inv_fact[i-1] = inv_fact[i]*i%MOD

m = int(input())
ans = []

for _ in range(m):
    n, k = map(int, input().split())

    result = fact[n]*inv_fact[k]%MOD
    result = result*inv_fact[n-k]%MOD

    ans.append(str(result))

print('\n'.join(ans))