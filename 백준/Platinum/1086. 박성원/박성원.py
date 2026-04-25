import sys
from math import gcd, factorial

input = sys.stdin.readline

n = int(input())
nums = [input().strip() for _ in range(n)]
k = int(input())

num_mod = [0]*n
ten_power_mod = [0]*n

for i in range(n):
    value = 0
    for ch in nums[i]:
        value = (value*10 + int(ch))%k

    num_mod[i] = value
    ten_power_mod[i] = pow(10, len(nums[i]), k)

transition = [[0]*k for _ in range(n)]
for i in range(n):
    for rem in range(k):
        transition[i][rem] = (rem*ten_power_mod[i]+num_mod[i])%k

size = 1 << n
full_mask = size - 1

bits = [1<<i for i in range(n)]
moves = [[] for _ in range(size)]

for mask in range(size):
    for i in range(n):
        if mask & bits[i] == 0:
            next_mask = mask | bits[i]
            moves[mask].append((i, next_mask))

cur = {0: [0]*k}
active = {0: [0]}

cur[0][0] = 1

for step in range(n):
    next_cur = {}
    next_active = {}

    for mask, row in cur.items():
        active_remainders = active[mask]
        for i, next_mask in moves[mask]:
            if next_mask not in next_cur:
                next_cur[next_mask] = [0]*k
                next_active[next_mask] = []

            next_row = next_cur[next_mask]
            next_active_remainders = next_active[next_mask]

            for rem in active_remainders:
                count = row[rem]

                next_rem = transition[i][rem]
                if next_row[next_rem] == 0:
                    next_active_remainders.append(next_rem)

                next_row[next_rem] += count

    cur = next_cur
    active = next_active

numerator = cur[full_mask][0]
denominator = factorial(n)

g = gcd(numerator, denominator)
numerator //= g
denominator //= g

print(f"{numerator}/{denominator}")