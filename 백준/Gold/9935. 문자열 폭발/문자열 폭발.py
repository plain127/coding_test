import sys

input = sys.stdin.readline

st = input().strip()
ex = input().strip()

n = len(ex)
last = ex[-1]
stack = []

for s in st:
    stack.append(s)

    match = False
    if len(stack) >= n and s == last:
        match = True
        for i in range(n):
            if stack[-n+i] != ex[i]:
                match = False
                break
    
    if match:
        for _ in range(n):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')