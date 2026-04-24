import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
planets = []

for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x,y,z,i))

edges = []

for axis in range(3):
    planets.sort(key=lambda p: p[axis])

    for i in range(n-1):
        p1 = planets[i]
        p2 = planets[i+1]

        cost = abs(p1[axis]-p2[axis])
        edges.append((cost, p1[3], p2[3]))

edges.sort()

parent = list(range(n))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return False

    parent[rb] = ra
    return True

ans = 0
edge_cnt = 0

for cost, a, b in edges:
    if union(a,b):
        ans += cost
        edge_cnt += 1

        if edge_cnt == n-1:
            break

print(ans)