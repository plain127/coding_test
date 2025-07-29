import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
seq = deque([int(input()) for _ in range(n)])

stack = []
lst = []
result = []

for i in range(1,n+1):
    stack.append(i)
    result.append('+')
    
    while stack:
        if stack[-1] != seq[0]:
            break
        lst.append(stack.pop())
        seq.popleft()
        result.append('-')

if seq:
    print('NO')
else:
    for r in result:
        print(r)