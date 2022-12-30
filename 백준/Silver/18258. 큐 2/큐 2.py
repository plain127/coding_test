import sys
from collections import deque
q = deque([])
N= int(sys.stdin.readline())
for i in range(N):
    cmd = sys.stdin.readline().split() 
    if cmd[0] == 'push':
            q.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif cmd[0] == 'size':
            print(len(q))
    elif cmd[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif cmd[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])