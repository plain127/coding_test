import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.buffer.readline

INF = 10**18

n, m = map(int, input().split())

arr = [0] + [int(input()) for _ in range(n)]

min_tree = [INF] * (4 * n)
max_tree = [-INF] * (4 * n)

def build(node, start, end):
    if start == end:
        min_tree[node] = arr[start]
        max_tree[node] = arr[start]
        return

    mid = (start + end) // 2

    build(node * 2, start, mid)
    build(node * 2 + 1, mid + 1, end)

    min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1])
    max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1])


def query(node, start, end, left, right):
    if right < start or end < left:
        return INF, -INF

    if left <= start and end <= right:
        return min_tree[node], max_tree[node]

    mid = (start + end) // 2

    left_min, left_max = query(node * 2, start, mid, left, right)
    right_min, right_max = query(node * 2 + 1, mid + 1, end, left, right)

    return min(left_min, right_min), max(left_max, right_max)


build(1, 1, n)

answer = []

for _ in range(m):
    a, b = map(int, input().split())
    mn, mx = query(1, 1, n, a, b)
    answer.append(f"{mn} {mx}")

print("\n".join(answer))