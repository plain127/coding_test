import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    d, a, b = map(int,input().split())

    if d == 0:
        union_parent(parent, a, b)
    elif d == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')