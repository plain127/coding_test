n = int(input())
edge = int(input())
node = [[] for i in range(n+1)]

visited = [0] * (n + 1)

for i in range(edge):
    x, y = map(int, input().split())
    node[x]+=[y]
    node[y]+=[x]

def dfs(node, v, visited):
    visited[v] = 1
    for i in node[v]:
        if not visited[i]:
            dfs(node, i, visited)

dfs(node, 1, visited)
print(sum(visited)-1)