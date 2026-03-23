import sys, heapq

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

weights = list(map(int, input().split()))

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

INF = int(1e9)

def dijkstra(start):
    distance = [INF]*(n+1)

    q = [(0, start)]
    distance[start] = 0

    while q:
        edge, node = heapq.heappop(q)

        if edge > distance[node]:
            continue

        for nxt, w in graph[node]:
            sums = w + edge
            if sums < distance[nxt]:
                distance[nxt] = sums
                heapq.heappush(q, (sums, nxt))

    prices = 0
    for i in range(1, n+1):
        if distance[i] <= m:
            prices += weights[i-1]

    return prices

max_price = 0
for i in range(1, n+1):
    max_price = max(max_price, dijkstra(i))

print(max_price)