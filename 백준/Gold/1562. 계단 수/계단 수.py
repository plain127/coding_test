import sys

input = sys.stdin.readline

MOD = 1000000000
n = int(input())

if n < 10:
    print(0)
    sys.exit()

FULL = (1<<10)-1

dp = [[[0]*(1<<10) for _ in range(10)] for _ in range(n+1)]

for d in range(1,10):
    dp[1][d][1<<d] = 1

for length in range(1,n):
    for last in range(10):
        cur = dp[length][last]

        if last > 0:
            nxt = last-1
            bit = 1<<nxt
            nxt_arr = dp[length+1][nxt]

            for mask in range(1<<10):
                if cur[mask]:
                    nxt_arr[mask|bit] = (nxt_arr[mask|bit] + cur[mask])%MOD

        if last < 9:
            nxt = last+1
            bit = 1<<nxt
            nxt_arr = dp[length+1][nxt]

            for mask in range(1<<10):
                if cur[mask]:
                    nxt_arr[mask|bit] = (nxt_arr[mask|bit] + cur[mask])%MOD

ans = 0
for last in range(10):
    ans = (ans+dp[n][last][FULL])%MOD

print(ans)