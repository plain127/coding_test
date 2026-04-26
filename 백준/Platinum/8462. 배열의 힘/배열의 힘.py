import sys

input = sys.stdin.buffer.readline

n, q = map(int, input().split())
arr = [0] + list(map(int, input().split()))

block = int(n ** 0.5) + 1

queries = []

for idx in range(q):
    left, right = map(int, input().split())
    block_id = left // block

    order_right = right if block_id % 2 == 0 else -right

    queries.append((block_id, order_right, left, right, idx))

queries.sort()

max_value = max(arr)
count = [0] * (max_value + 1)

answers = [0] * q
power = 0


def add(value):
    global power

    c = count[value]
    power += (2 * c + 1) * value
    count[value] = c + 1


def remove(value):
    global power

    c = count[value]
    power -= (2 * c - 1) * value
    count[value] = c - 1


cur_left = 1
cur_right = 0

for _, _, left, right, query_id in queries:
    while cur_left > left:
        cur_left -= 1
        add(arr[cur_left])

    while cur_right < right:
        cur_right += 1
        add(arr[cur_right])

    while cur_left < left:
        remove(arr[cur_left])
        cur_left += 1

    while cur_right > right:
        remove(arr[cur_right])
        cur_right -= 1

    answers[query_id] = power

sys.stdout.write('\n'.join(map(str, answers)))