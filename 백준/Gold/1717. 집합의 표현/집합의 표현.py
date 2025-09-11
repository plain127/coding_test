import sys 

input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n+1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a,b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra

for _ in range(m):
    check, a, b = map(int, input().split())
    if check == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')
