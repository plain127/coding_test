import sys

input = sys.stdin.readline

n = int(input())
a0, a1, a2 = map(int, input().split())

max0 = a0
max1 = a1
max2 = a2

min0 = a0
min1 = a1
min2 = a2

for _ in range(n-1):
    b0, b1, b2 = map(int, input().split())

    
    c0 = max(max0, max1) + b0
    c1 = max(max0, max1, max2) + b1
    c2 = max(max1, max2) + b2

    d0 = min(min0, min1) + b0
    d1 = min(min0, min1, min2) + b1
    d2 = min(min1, min2) + b2

    max0, max1, max2 = c0, c1, c2
    min0, min1, min2 = d0, d1, d2

print(max(max0, max1, max2), min(min0, min1, min2))