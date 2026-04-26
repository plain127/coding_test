import sys

input = sys.stdin.readline

n = int(input())
energy = [0]

for _ in range(n):
    energy.append(int(input()))

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

log = n.bit_length()
parent = [[0]*(n+1) for _ in range(log)]
dist = [[0]*(n+1) for _ in range(log)]

stack = [1]
visited = [False]*(n+1)
visited[1] = True

while stack:
    room = stack.pop()

    for nxt, cost in graph[room]:
        if visited[nxt]:
            continue

        parent[0][nxt] = room
        dist[0][nxt] = cost

        visited[nxt] = True
        stack.append(nxt)

for k in range(1, log):
    for room in range(1,n+1):
        mid = parent[k-1][room]
        parent[k][room] = parent[k-1][mid]
        dist[k][room] = dist[k-1][room] + dist[k-1][mid]

def climb(room, power):
    current = room

    for k in range(log-1, -1, -1):
        jump_to = parent[k][current]

        if jump_to != 0 and dist[k][current] <= power:
            power -= dist[k][current]
            current = jump_to
    
    return current

ans = []

for room in range(1,n+1):
    result = climb(room, energy[room])
    ans.append(str(result))

print('\n'.join(ans))