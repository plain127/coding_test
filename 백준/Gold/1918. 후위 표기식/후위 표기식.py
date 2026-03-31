import sys

input = sys.stdin.readline

st = input().strip()

stack = []

def priority(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

for s in st:
    if s.isalpha():
        print(s, end="")
    
    elif s == '(':
        stack.append(s)

    elif s == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()

    else:
        while stack and stack[-1] != '(' and priority(stack[-1]) >= priority(s):
            print(stack.pop(), end='')
        stack.append(s)
        
while stack:
    print(stack.pop(), end="")
