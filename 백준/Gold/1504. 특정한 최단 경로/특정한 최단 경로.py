import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c =  map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for next, val  in graph[now]:
            if distance[next] > distance[now] + val:
                distance[next] = distance[now] + val
                heapq.heappush(q,(distance[next], next))

    return distance[end]

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))