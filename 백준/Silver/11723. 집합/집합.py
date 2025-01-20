import sys

input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    order = input().split()

    if order[0] == 'add':
        s.add(int(order[1]))
    elif order[0] == 'remove':
        try:
            s.remove(int(order[1]))
        except:
            pass
    elif order[0] == 'check':
        if int(order[1]) in s:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if int(order[1]) in s:
            s.remove(int(order[1]))
        else:
            s.add(int(order[1]))
    elif order[0] == 'all':
        s = set([i for i in range(1,21)])
    elif order[0] == 'empty':
        s = set()