import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(n))

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

result = 0
for turn in range(1, m+1):
    a, b = map(int, input().split())
    if not union(a, b):
        result = turn
        break

print(result)