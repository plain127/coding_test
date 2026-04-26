import sys

input = sys.stdin.buffer.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

m = int(input())
block = int(n ** 0.5) + 1

queries = []

for query_id in range(m):
    left, right = map(int, input().split())
    block_id = left // block

    order_right = right if block_id % 2 == 0 else -right

    queries.append((block_id, order_right, left, right, query_id))

queries.sort()

MAX_VALUE = 100000
cnt = [0] * (MAX_VALUE + 1)

freq = [0] * (n + 1)

answers = [0] * m
current_max = 0


def add(value):
    global current_max

    old = cnt[value]

    if old > 0:
        freq[old] -= 1

    new = old + 1
    cnt[value] = new
    freq[new] += 1

    if new > current_max:
        current_max = new


def remove(value):
    global current_max

    old = cnt[value]
    freq[old] -= 1

    new = old - 1
    cnt[value] = new

    if new > 0:
        freq[new] += 1

    while current_max > 0 and freq[current_max] == 0:
        current_max -= 1


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

    answers[query_id] = current_max

sys.stdout.write('\n'.join(map(str, answers)))