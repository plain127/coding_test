import sys

input = sys.stdin.readline

n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = list(range(n+1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return False
    
    parent[rb] = ra
    return True

total = 0
cnt = 0

for cost, a, b in edges:
    if union(a,b):
        total += cost
        cnt = cost

print(total-cnt)