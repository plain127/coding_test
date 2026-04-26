import sys

input = sys.stdin.buffer.readline


def add(index, value):
    while index <= n:
        bit[index] += value
        index += index & -index


def prefix_sum(index):
    total = 0

    while index > 0:
        total += bit[index]
        index -= index & -index

    return total


n = int(input())
arr = [0] + list(map(int, input().split()))

q = int(input())
queries = []

for query_id in range(q):
    left, right = map(int, input().split())
    queries.append((right, left, query_id))

queries.sort()

bit = [0] * (n + 1)
last = {}
answers = [0] * q

cur_right = 0

for_right_loop = queries
for right, left, query_id in for_right_loop:
    while cur_right < right:
        cur_right += 1
        value = arr[cur_right]

        if value in last:
            add(last[value], -1)

        add(cur_right, 1)
        last[value] = cur_right

    answers[query_id] = prefix_sum(right) - prefix_sum(left - 1)

sys.stdout.write('\n'.join(map(str, answers)))