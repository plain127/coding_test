import sys

input = sys.stdin.readline

n = int(input())
liq = list(map(int, input().split()))
liq.sort()

best = 10**18
ans1 = ans2 = ans3 = 0

for i in range(n - 2):
    fixed = liq[i]

    # 만들 수 있는 최소합
    min_sum = fixed + liq[i + 1] + liq[i + 2]
    if min_sum > 0:
        if min_sum < best:
            best = min_sum
            ans1, ans2, ans3 = fixed, liq[i + 1], liq[i + 2]
        break

    # 만들 수 있는 최대합
    max_sum = fixed + liq[n - 2] + liq[n - 1]
    if max_sum < 0:
        if -max_sum < best:
            best = -max_sum
            ans1, ans2, ans3 = fixed, liq[n - 2], liq[n - 1]
        continue

    left = i + 1
    right = n - 1

    while left < right:
        total = fixed + liq[left] + liq[right]
        cur = total if total >= 0 else -total

        if cur < best:
            best = cur
            ans1, ans2, ans3 = fixed, liq[left], liq[right]
            if best == 0:
                print(ans1, ans2, ans3)
                sys.exit(0)

        if total < 0:
            left += 1
        else:
            right -= 1

print(ans1, ans2, ans3)