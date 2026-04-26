import sys

input = sys.stdin.readline

INF = 10**15

n, m = map(int, input().split())
dist = [[INF]*(n+1) for _ in range(n+1)]
edges = []

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, length = map(int, input().split())

    edges.append((a,b,length))

    if length < dist[a][b]:
        dist[a][b] = length
        dist[b][a] = length

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            new_dist = dist[i][k] + dist[k][j]

            if new_dist < dist[i][j]:
                dist[i][j] = new_dist

best = INF

for start in range(1,n+1):
    current = 0

    for a, b, length in edges:
        left = dist[start][a]
        right = dist[start][b]

        burn_time = left + right + length

        if current < burn_time:
            current = burn_time

    if current < best:
        best = current
    
if best%2 == 0:
    print(f'{best//2}.0')
else:
    print(f'{best//2}.5')