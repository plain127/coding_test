class Stack:
    def __init__(self):
        self.top = []
    def isEmpty(self):
        return len(self.top)==0
    def size(self):
        return len(self.top)
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

K=int(input())
stack = Stack()
if K>=1 and K<=100000:
    for i in range(K):
        ask = int(input())
        if ask == 0:
            stack.pop()
        elif ask >= 1000000:
            break
        else:
            stack.push(ask)
    sum = 0
    for i in range(stack.size()):
        sum += stack.pop()
    print(sum)
