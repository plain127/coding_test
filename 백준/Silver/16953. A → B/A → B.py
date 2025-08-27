import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())

q = deque([(a, 1)])
answer = -1

while q:
    num, cnt = q.popleft()
    
    if num == b:
        answer = cnt
        break
    
    for n in 2*num, 10*num+1:
        if n <= b:
            q.append((n, cnt+1))

print(answer)