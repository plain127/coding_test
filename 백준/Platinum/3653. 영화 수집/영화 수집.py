import sys

input = sys.stdin.readline

all_answers = []
t = int(input())

def update(tree, size, position, value):
    idx = size + position - 1
    tree[idx] = value
    idx //= 2

    while idx:
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
        idx //= 2


def query(tree, size, left, right):
    if left > right:
        return 0

    left = size + left - 1
    right = size + right - 1

    total = 0

    while left <= right:
        if left % 2 == 1:
            total += tree[left]
            left += 1

        if right % 2 == 0:
            total += tree[right]
            right -= 1

        left //= 2
        right //= 2

    return total


for _ in range(t):
    n, m = map(int, input().split())

    movies = list(map(int, input().split()))

    total_size = n + m

    size = 1

    while size < total_size:
        size *= 2

    tree = [0] * (size * 2)

    pos = [0] * (n + 1)

    for movie in range(1, n + 1):
        position = m + movie
        pos[movie] = position
        update(tree, size, position, 1)

    top = m
    answer = []

    for movie in movies:
        position = pos[movie]

        count_above = query(tree, size, 1, position - 1)

        answer.append(str(count_above))

        update(tree, size, position, 0)

        update(tree, size, top, 1)

        pos[movie] = top

        top -= 1

    all_answers.append(' '.join(answer))

print('\n'.join(all_answers))