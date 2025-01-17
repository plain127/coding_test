#내 풀이
import sys

input = sys.stdin.readline

x = int(input())

count = [0]*30001

for i in range(2, x+1):
    a = 30001
    b = 30001
    c = 30001
    if i%5 == 0:
        a = count[i//5] + 1
    elif i%3 == 0:
        b = count[i//3] + 1
    elif i%2 == 0:
        c = count[i//2] + 1
    d = count[i-1] + 1

    count[i] = min(a, b, c, d)

print(count[x])

#책 풀이
x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])