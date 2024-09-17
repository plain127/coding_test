from collections import deque
n = int(input())
nums= deque()
nums_sort = []
stack = []
results = []

for _ in range(n):
    num = int(input())
    nums.append(num)
    nums_sort.append(num)
    
nums_sort.sort(reverse=True)

while len(nums_sort) > 0:
    if len(stack) == 0:
        stack.append(nums_sort.pop())
        results.append('+')
    else:
        if stack[-1] != nums[0]:
            stack.append(nums_sort.pop())
            results.append('+')
        else:
            stack.pop()
            nums.popleft()
            results.append('-')
            
while len(stack) > 0:
    if stack.pop() != nums.popleft():
        print('NO')
        break
    else:
        results.append('-')

if len(stack) == 0:
    for result in results:
        print(result)