import sys
from collections import deque

n = int(sys.stdin.readline().strip())
q = deque()
results = []

for _ in range(n):
    order = sys.stdin.readline().strip().split()
    if order[0] == 'push':
        q.append(int(order[1]))
    elif order[0] == 'pop':
        if len(q) == 0:
            results.append(-1)
        else:
            results.append(q.popleft())
    elif order[0] == 'size':
        results.append(len(q))
    elif order[0] == 'empty':
        if len(q) == 0:
            results.append(1)
        else:
            results.append(0)
    elif order[0] == 'front':
        if len(q) == 0:
            results.append(-1)
        else:
            results.append(q[0])
    elif order[0] == 'back':
        if len(q) == 0:
            results.append(-1)
        else:
            results.append(q[-1])
            
for result in results:
    print(result)