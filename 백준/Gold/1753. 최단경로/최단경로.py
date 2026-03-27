import sys, heapq

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(e):
    u, y, w = map(int, input().split())
    graph[u].append((y, w))

INF = int(1e9)
distance = [INF]*(v+1)

q = [(0, k)]
distance[k] = 0

while q:
    weight, node = heapq.heappop(q)

    if weight > distance[node]:
        continue

    for nxt, w in graph[node]:
        sums = weight + w
        if sums < distance[nxt]:
            distance[nxt] = sums
            heapq.heappush(q, (sums, nxt))

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])