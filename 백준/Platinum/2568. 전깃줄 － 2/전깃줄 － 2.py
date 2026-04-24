import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
wires = []

for _ in range(n):
    a, b = map(int, input().split())
    wires.append((a, b))

wires.sort()


tails = []
tails_idx = []
prev = [-1] * n

for i in range(n):
    a, b = wires[i]
    pos = bisect_left(tails, b)

    if pos > 0:
        prev[i] = tails_idx[pos - 1]

    if pos == len(tails):
        tails.append(b)
        tails_idx.append(i)

    else:
        tails[pos] = b
        tails_idx[pos] = i

keep = [False] * n

cur = tails_idx[-1]

while cur != -1:
    keep[cur] = True
    cur = prev[cur]

removed = []

for i in range(n):
    if not keep[i]:
        removed.append(wires[i][0])


print(len(removed))

for a in removed:
    print(a)