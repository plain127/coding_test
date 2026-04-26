import sys

input = sys.stdin.readline

D, P, Q = map(int, input().split())

if P < Q:
    P, Q = Q, P

answer = 10 ** 30

limit = min(Q - 1, D // P + 1)

for p_count in range(limit + 1):
    p_money = p_count * P

    if p_money >= D:
        answer = min(answer, p_money)
        continue

    remain = D - p_money

    q_count = (remain + Q - 1) // Q

    total = p_money + q_count * Q

    answer = min(answer, total)

print(answer)