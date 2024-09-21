import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
#in_file = open('input.txt', 'r')

def dfs(visited, graph, v):
    global count
    visited[v] = count
    count += 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(visited, graph, i)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0]*(n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,len(graph)):
    graph[i].sort()

count = 1
dfs(visited, graph, r)

for i in range(1,n+1):
    print(visited[i])