import sys
from math import gcd

input = sys.stdin.buffer.readline


def bit_add(index, value):
    while index <= n:
        bit[index] += value
        index += index & -index


def bit_prefix(index):
    total = 0

    while index > 0:
        total += bit[index]
        index -= index & -index

    return total


def bit_range_add(left, right, value):
    bit_add(left, value)

    if right + 1 <= n:
        bit_add(right + 1, -value)


def seg_set(position, value):
    node = size + position - 1
    seg[node] = abs(value)

    node //= 2

    while node:
        seg[node] = gcd(seg[node * 2], seg[node * 2 + 1])
        node //= 2


def seg_query(left, right):
    if left > right:
        return 0

    left = size + left - 1
    right = size + right - 1

    result = 0

    while left <= right:
        if left % 2 == 1:
            result = gcd(result, seg[left])
            left += 1

        if right % 2 == 0:
            result = gcd(result, seg[right])
            right -= 1

        left //= 2
        right //= 2

    return result


n = int(input())
arr = [0] + list(map(int, input().split()))

bit = [0] * (n + 2)

for i in range(1, n + 1):
    bit_range_add(i, i, arr[i])

diff = [0] * (n + 2)

for i in range(1, n + 1):
    diff[i] = arr[i] - arr[i - 1]

size = 1

while size < n:
    size <<= 1

seg = [0] * (size * 2)

for i in range(1, n + 1):
    seg[size + i - 1] = abs(diff[i])

for node in range(size - 1, 0, -1):
    seg[node] = gcd(seg[node * 2], seg[node * 2 + 1])

q = int(input())
answer = []

for _ in range(q):
    t, left, right = map(int, input().split())

    if t == 0:
        first_value = bit_prefix(left)
        diff_gcd = seg_query(left + 1, right)
        answer.append(str(gcd(abs(first_value), diff_gcd)))

    else:
        bit_range_add(left, right, t)

        diff[left] += t
        seg_set(left, diff[left])

        if right + 1 <= n:
            diff[right + 1] -= t
            seg_set(right + 1, diff[right + 1])

sys.stdout.write('\n'.join(answer))