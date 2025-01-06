import sys

input = sys.stdin.readline

n = int(input())

count = 0
f = [0]*(n+1)
def fibonacci(n):
    global count

    f[1] = 1
    f[2] = 1
    
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        count += 1
    return f[n]

print(f'{fibonacci(n)} {count}')