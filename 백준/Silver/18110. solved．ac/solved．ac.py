import sys

input = sys.stdin.readline

def up(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())

if n==0:
    print(0)
else:
    di = []

    for _ in range(n):
        di.append(int(input()))

    di.sort()
    x = up(n*0.15)

    print(up(sum(di[x:n-x])/len(di[x:n-x])))