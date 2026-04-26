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

    # 짝수 블록은 right 오름차순, 홀수 블록은 right 내림차순
    # 포인터 왕복을 줄이는 Mo 정렬 트릭
    order_right = right if block_id % 2 == 0 else -right

    queries.append((block_id, order_right, left, right, query_id))

queries.sort()

MAX_VALUE = 1_000_000
count = [0] * (MAX_VALUE + 1)

answers = [0] * m
distinct = 0


def add(value):
    global distinct

    if count[value] == 0:
        distinct += 1

    count[value] += 1


def remove(value):
    global distinct

    count[value] -= 1

    if count[value] == 0:
        distinct -= 1


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

    answers[query_id] = distinct

sys.stdout.write('\n'.join(map(str, answers)))