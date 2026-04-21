import sys

input = sys.stdin.readline

g = int(input())
p = int(input())

parent = list(range(g+1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

ans = 0

for _ in range(p):
    gi = int(input())
    dock = find(gi)

    if dock == 0:
        break

    ans += 1
    parent[dock] = find(dock-1)

print(ans)