import sys

input = sys.stdin.readline

n = int(input())
co = []

for _ in range(n):
    x, y = map(int, input().split())
    co.append((x, y))

co.sort()
co.sort(key=lambda x : x[1])

for c in co:
    x,y = c
    print(x, y)