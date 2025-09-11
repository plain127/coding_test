from re import L
import sys 

input = sys.stdin.readline

n = int(input())
m = int(input())

parent = list(range(n+1))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra

for i in range(1, n+1):
    row = list(map(int, input().split()))
    for idx, v in enumerate(row, start=1):
        if v == 1:
            union(i, idx)

plan = list(map(int, input().split()))
root = find(plan[0])

ok = all(find(city) == root for city in plan[1:])

print('YES' if ok else 'NO')