import sys, heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e,c))

start, end = map(int, input().split())

INF = int(1e9)
dist = [INF]*(n+1)
parent = [0]*(n+1)

q = [(0, start)]
dist[start] = 0

while q:
    cost, node = heapq.heappop(q)

    if cost > dist[node]:
        continue

    for nxt, c in graph[node]:
        sums = cost+c
        if sums < dist[nxt]:
            dist[nxt] = sums
            parent[nxt] = node
            heapq.heappush(q, (sums, nxt))

path = []
nxt = end
while nxt != 0:
    path.append(nxt)
    nxt = parent[nxt]
path.reverse()

print(dist[end])
print(len(path))
print(*path)