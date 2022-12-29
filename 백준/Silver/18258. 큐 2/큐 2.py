import sys
from collections import deque
q=deque([])
N=int(sys.stdin.readline())
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        if len(q) != 0 :
            print(q.popleft())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)