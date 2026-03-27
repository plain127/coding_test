import sys, heapq

input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

INF = int(1e9)

def dijkstra(start, end):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = [(0, start)]

    while q:
        weight, node = heapq.heappop(q)

        if weight > distance[node]:
            continue

        for nxt, w in graph[node]:
            sums = weight + w
            if sums < distance[nxt]:
                distance[nxt] = sums
                heapq.heappush(q, (sums, nxt))
    
    return distance[end]

d1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
d2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

dis = min(d1, d2)
if dis >= INF:
    print(-1)
else:
    print(dis)