import sys

n = int(input())

queue = []
for i in range(n):
    input_word = sys.stdin.readline().split()

    if input_word[0] == 'push':
        queue.append(input_word[1])

    elif input_word[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    
    elif input_word[0] == 'size':
        print(len(queue))
    
    elif input_word[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif input_word[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif input_word[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])