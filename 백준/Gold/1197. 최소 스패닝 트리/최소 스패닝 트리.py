import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v, e = map(int, input().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = list(range(v+1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
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
        cnt += 1
        if cnt == v-1:
            break

print(total)