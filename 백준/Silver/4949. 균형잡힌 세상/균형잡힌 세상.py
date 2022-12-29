import sys
input = sys.stdin.readline
 
while 1:
    string = input().rstrip()
    stack = []
    check = 1
 
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                check = 0
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                check = 0
                break
 
    if string == '.':
        break
 
    print("yes" if check and not stack else "no")
