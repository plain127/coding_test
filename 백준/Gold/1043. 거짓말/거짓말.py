import sys

input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int ,input().split()))
truth = set(t[1:])

party = []
for _ in range(m):
    data = list(map(int, input().split()))
    party.append(data[1:])

parent = list(range(n+1))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra != rb:
        parent[rb] = ra

for p in party:
    for i in range(1, len(p)):
        union(p[0], p[i])

truth_roots = {find(x) for x in truth}
ans = 0
for p in party:
    if all(find(pp) not in truth_roots for pp in p):
        ans += 1

print(ans)