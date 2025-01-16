import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
counts = []

for _ in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))

    count = 0
    target = q[m]
    idx = m

    while q:
        if q[0] == target and idx == 0:
            if max(q) == target:
                count += 1
                break
            else:
                q.append(q[0])
                q.popleft()
                idx = len(q) - 1
        elif q[0] == target and idx != 0:
            if q[0] == max(q):
                q.popleft()
                count += 1
                idx -= 1
            else:
                q.append(q[0])
                q.popleft()
                idx -= 1

        elif q[0] != target:
            if q[0] == max(q):
                q.popleft()
                count += 1
                idx -= 1
            else:
                q.append(q[0])
                q.popleft()
                idx -= 1

    counts.append(count)

for count in counts:
    print(count)