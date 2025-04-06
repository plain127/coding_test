import sys
from collections import deque

input = sys.stdin.readline
results = []

for _ in range(int(input())):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    idx = m
    count = 0

    while q:
        if q[0] < max(q):
            doc = q.popleft()
            if idx == 0:
                q.append(doc)
                idx = len(q)-1
            else:
                q.append(doc)
                idx -= 1
        
        else: 
            if idx != 0 and q[0] == max(q):
                q.popleft()
                idx -= 1
                count += 1

            elif idx == 0 and q[0] == max(q):
                count += 1 
                break

    results.append(count)

for result in results:
    print(result)