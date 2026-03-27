import sys, heapq

input = sys.stdin.readline

n, m, r = map(int, input().split())
t = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

INF = int(1e9)

def dijkstra(start):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = [(0, start)]

    while q:
        weight, node = heapq.heappop(q)
        
        if weight > distance[node]:
            continue

        for nxt, dw in graph[node]:
            sums = weight + dw 
            if sums < distance[nxt]:
                distance[nxt] = sums
                heapq.heappush(q, (sums, nxt))

    item = 0
    for i in range(1, n+1):
        if distance[i] <= m:
            item += t[i-1] 
    
    return item

item = 0
for i in range(1, n+1):
    item = max(dijkstra(i), item)

print(item)