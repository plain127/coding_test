import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, n+1):
    graph[i].sort(reverse=True)

visited = [0]*(n+1)
count = 1

def dfs(r):
    global count 
    visited[r] += count
    count += 1
    
    for i in graph[r]:
        if visited[i] == 0:
            dfs(i)
dfs(r)
for i in range(1,n+1):
    print(visited[i])