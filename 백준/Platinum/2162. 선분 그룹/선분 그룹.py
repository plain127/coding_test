from re import L
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
seg = []

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    seg.append(((x1, y1), (x2, y2)))

def ccw(a,b,c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    value = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0

def is_intersect(seg1, seg2):
    a, b = seg1
    c, d = seg2

    ab = ccw(a,b,c)*ccw(a,b,d)
    cd = ccw(c,d,a)*ccw(c,d,b)

    if ab == 0 and cd == 0:
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        
        return c <= b and a <= d
    return ab <= 0 and cd <= 0

parent = list(range(n))
size = [1]*n

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a,b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return

    if size[ra] < size[rb]:
        ra, rb = rb, ra

    parent[rb] = ra
    size[ra] += size[rb]

for i in range(n):
    for j in range(i+1, n):
        if is_intersect(seg[i], seg[j]):
            union(i,j)

group_cnt = 0
max_group_size = 0

for i in range(n):
    if find(i) == i:
        group_cnt += 1
        max_group_size = max(max_group_size, size[i])

print(group_cnt)
print(max_group_size)