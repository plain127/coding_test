import sys

n = int(sys.stdin.readline().strip())
stack = []
results = []

for _ in range(n):
    order = sys.stdin.readline().strip().split()
    if order[0] == '1':
       stack.append(int(order[1]))
    elif order[0] == '2':
        if len(stack) == 0:
            results.append(-1)
        else:
            results.append(stack.pop())
    elif order[0] == '3':
        results.append(len(stack))
    elif order[0] == '4':
        if len(stack) == 0:
            results.append(1)
        else:
            results.append(0)
    elif order[0] == '5':
        if len(stack) == 0:
            results.append(-1)
        else:
            results.append(stack[-1])

for result in results:
    print(result)