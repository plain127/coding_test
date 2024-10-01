import sys
from collections import deque
#in_file = open('input.txt', 'r')

def dfs(graph, start, visited, result):
    visited[start] = True
    result.append(start)
    
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited, result)
            
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    result = []
    while queue:
        v = queue.popleft()
        result.append(v)
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    
    return result

def return_dfs(graph, v):
    visited = [False]*len(graph)
    result = []
    dfs(graph, v, visited, result)
    return result
    
def return_bfs(graph, v):
    visited = [False]*len(graph)
    return bfs(graph, v, visited)    
    
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()
    
first = return_dfs(graph, v)
second = return_bfs(graph, v)

print(' '.join(map(str, first)))
print(' '.join(map(str, second)))