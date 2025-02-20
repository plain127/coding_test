import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)

for _ in range(e):
    u, y, w = map(int, input().split())
    graph[u].append((y,w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(k)

for i in range(1, v+1): 
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])