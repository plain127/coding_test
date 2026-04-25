import sys

input = sys.stdin.readline

mx = 1000000

tr = [0] * (mx * 4)


def upd(node, l, r, x, v):
    if l == r:
        tr[node] += v
        return

    mid = (l + r) // 2

    if x <= mid:
        upd(node * 2, l, mid, x, v)
    else:
        upd(node * 2 + 1, mid + 1, r, x, v)

    tr[node] = tr[node * 2] + tr[node * 2 + 1]


def kth(node, l, r, k):
    if l == r:
        return l

    mid = (l + r) // 2

    left_cnt = tr[node * 2]

    if k <= left_cnt:
        return kth(node * 2, l, mid, k)

    return kth(node * 2 + 1, mid + 1, r, k - left_cnt)


n = int(input())
ans = []

for _ in range(n):
    q = list(map(int, input().split()))

    if q[0] == 1:
        b = q[1]

        x = kth(1, 1, mx, b)

        ans.append(str(x))

        upd(1, 1, mx, x, -1)

    else:
        b = q[1]
        c = q[2]

        upd(1, 1, mx, b, c)

print("\n".join(ans))