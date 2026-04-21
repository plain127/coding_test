import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

hq = []
for i in range(1,n+1):
    if indegree[i] == 0:
        hq.append(i)

ans = []
while hq:
    cur = heapq.heappop(hq)
    ans.append(cur)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(hq, nxt)

print(*ans)