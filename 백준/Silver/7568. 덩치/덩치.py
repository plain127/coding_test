import sys

input = sys.stdin.readline

n = int(input())
d = []

for _ in range(n):
    x, y = map(int, input().split())
    d.append((x, y))

result = []

for i in range(n):
    count = 1
    x1, y1 = d[i]
    for j in range(n):
        x2, y2 = d[j]
        if x1 < x2 and y1 < y2:
            count += 1
    result.append(count)        

for i in result:
    print(i, end =' ')