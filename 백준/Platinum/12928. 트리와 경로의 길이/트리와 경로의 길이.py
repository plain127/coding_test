import sys

input = sys.stdin.readline

n, s = map(int, input().split())

if n == 1:
    print(1 if s == 0 else 0)
    sys.exit()

remain = n - 2

dp = [[False] * (s + 1) for _ in range(remain + 1)]
dp[0][0] = True

for used in range(remain + 1):
    for score in range(s + 1):
        if not dp[used][score]:
            continue

        for k in range(1, remain - used + 1):
            add_score = k * (k + 1) // 2
            next_score = score + add_score

            if next_score > s:
                break

            dp[used + k][next_score] = True

print(1 if dp[remain][s] else 0)