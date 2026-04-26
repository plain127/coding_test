import sys

input = sys.stdin.buffer.readline

INF = 10 ** 9

n = int(input())

first_order = list(map(int, input().split()))
second_order = list(map(int, input().split()))
third_order = list(map(int, input().split()))

rank2 = [0] * (n + 1)
rank3 = [0] * (n + 1)

for rank, student in enumerate(second_order, start=1):
    rank2[student] = rank

for rank, student in enumerate(third_order, start=1):
    rank3[student] = rank

tree = [INF] * (n + 1)


def update(index, value):
    while index <= n:
        if value < tree[index]:
            tree[index] = value
        index += index & -index


def query(index):
    result = INF

    while index > 0:
        if tree[index] < result:
            result = tree[index]
        index -= index & -index

    return result


answer = 0

for student in first_order:
    r2 = rank2[student]
    r3 = rank3[student]

    best_r3 = query(r2 - 1)

    if best_r3 > r3:
        answer += 1

    update(r2, r3)

print(answer)