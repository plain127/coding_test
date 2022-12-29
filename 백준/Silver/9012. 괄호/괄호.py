class Stack:
    def __init__(self):
        self.arr=[]
    def isEmpty(self):
        if len(self.arr) == 0:
            return 0
    def push(self,item):
        self.arr.append(item)
    def pop(self):
        if self.isEmpty() != 0:
            return self.arr.pop(-1)
    def clear(self):
        self.arr=[]

T = int(input())
stack = Stack()

for i in range(T):
    put = list(input())
    if len(put)>=2 and len(put)<=50:
        check = 0
        for j in range(len(put)):
            if put[j] == '(':
                stack.push(put[j])
            elif put[j] == ')':
                if stack.isEmpty() == 0:
                    check += 1
                    break
                else:
                    stack.pop()
        if stack.isEmpty() == 0 and check == 0:
            print('YES')
        else:
            print('NO')
            stack.clear()
