import sys

input = sys.stdin.readline

m = int(input())

MOD = 1000000007
ans = 0

for _ in range(m):
    n, s = map(int, input().split())
    ans = (ans + s*pow(n, MOD-2, MOD))%MOD

print(ans)