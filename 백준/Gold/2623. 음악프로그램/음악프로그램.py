import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    seq = list(map(int, input().split()))
    num = seq[0]
    for i in range(1, num):
        graph[seq[i]].append(seq[i+1])
        indegree[seq[i+1]] += 1

q = deque()
for x in range(1, n+1):
    if indegree[x] == 0:
        q.append(x)

result = []
while q:
    cur = q.popleft()
    result.append(cur)

    for nxt in graph[cur]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

if len(result) != n:
    print(0)
else:
    print(*result, sep='\n')