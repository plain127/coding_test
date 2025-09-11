import sys

input = sys.stdin.readline

n, m = map(int, input().split())
line = list(map(int, input().split()))
truth = set(line[1:])

parties = []
for _ in range(m):
    data = list(map(int, input().split()))
    parties.append(data[1:])

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

for ppl in parties:
    for i in range(1, len(ppl)):
        union(ppl[0], ppl[i])

truth_roots = {find(x) for x in truth}
ans = 0
for ppl in parties:
    if all(find(p) not in truth_roots for p in ppl):
        ans += 1

print(ans)