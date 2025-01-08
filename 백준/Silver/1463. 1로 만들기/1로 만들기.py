import sys

input = sys.stdin.readline

n = int(input())

count = [0]*1000001

for i in range(2, n+1):
    a = 1000001
    b = 1000001
    if i % 3 == 0:
        a = count[i//3] + 1
    if i % 2 == 0:
        b = count[i//2] + 1
    c = count[i-1] + 1

    count[i] = min(a, b, c)

print(count[n])