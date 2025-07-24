import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    p = input().strip()
    n = int(input()) 
    arr = input().strip()
   
    if n == 0:
        q = deque()
    else:
        q = deque(map(int, arr[1:-1].split(',')))

    rev = False
    error = False

    for i in p:
        if i == 'R':
            rev = not rev
        elif i == 'D':
            if not q:
                error = True
                break
            if not rev:
                q.popleft()
            else:
                q.pop()          
    
    if error:
        print('error')
    else:
        if rev:
            q.reverse()
        print('['+','.join(map(str, q))+']')