import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(int, input().split()))

positions = [[] for _ in range(c + 1)]

for index, color in enumerate(arr, start=1):
    positions[color].append(index)

size = 1

while size < n:
    size <<= 1

tree_color = [0] * (size * 2)
tree_count = [0] * (size * 2)


def merge(color1, count1, color2, count2):
    if count1 == 0:
        return color2, count2

    if count2 == 0:
        return color1, count1

    if color1 == color2:
        return color1, count1 + count2

    if count1 > count2:
        return color1, count1 - count2

    if count2 > count1:
        return color2, count2 - count1

    return 0, 0


for i in range(n):
    tree_color[size + i] = arr[i]
    tree_count[size + i] = 1

for node in range(size - 1, 0, -1):
    color, count = merge(
        tree_color[node * 2],
        tree_count[node * 2],
        tree_color[node * 2 + 1],
        tree_count[node * 2 + 1],
    )

    tree_color[node] = color
    tree_count[node] = count


def query(left, right):
    left += size - 1
    right += size - 1

    left_color = 0
    left_count = 0
    right_color = 0
    right_count = 0

    while left <= right:
        if left % 2 == 1:
            left_color, left_count = merge(
                left_color,
                left_count,
                tree_color[left],
                tree_count[left],
            )

            left += 1

        if right % 2 == 0:
            right_color, right_count = merge(
                tree_color[right],
                tree_count[right],
                right_color,
                right_count,
            )

            right -= 1

        left //= 2
        right //= 2

    final_color, final_count = merge(
        left_color,
        left_count,
        right_color,
        right_count,
    )

    return final_color


m = int(input())
answer = []

for _ in range(m):
    left, right = map(int, input().split())

    candidate = query(left, right)

    if candidate == 0:
        answer.append('no')
        continue

    color_positions = positions[candidate]

    count = bisect_right(color_positions, right) - bisect_left(color_positions, left)
    length = right - left + 1

    if count > length // 2:
        answer.append(f'yes {candidate}')
    else:
        answer.append('no')

sys.stdout.write('\n'.join(answer))