import sys, heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, p = map(int, input().split())
    graph[s].append((e, p))

start, end = map(int, input().split())

INF = int(1e9)
dist = [INF]*(n+1)

dist[start] = 0
pq = [(0, start)]

while pq:
    edge, node = heapq.heappop(pq)

    if edge > dist[node]:
        continue
    
    if node == end:
        break

    for nxt, price in graph[node]:
        price_sum = edge + price
        if price_sum < dist[nxt]:
            dist[nxt] = price_sum
            heapq.heappush(pq, (price_sum, nxt))

print(dist[end])