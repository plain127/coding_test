t = int(input())

for _ in range(t):
    ps = input()
    stack = []
    
    for p in ps:
        if p == '(':
            stack.append('(')
        elif p == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()
        
    if len(stack) != 0:
        print('NO')
    else:
        print('YES')