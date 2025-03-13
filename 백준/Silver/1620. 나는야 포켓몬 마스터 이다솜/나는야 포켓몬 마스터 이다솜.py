import sys

input = sys.stdin.readline

n, m = map(int, input().split())
docs = [0]*(n+1)
name_to_idx = {}

for i in range(1,n+1):
    name = input().strip()
    docs[i] = name
    name_to_idx[name] = i

results = []
for _ in range(m):
    q = input().strip()
    if q.isdigit():
        results.append(docs[int(q)])
    else:
        results.append(name_to_idx[q])

for result in results:
    print(result)