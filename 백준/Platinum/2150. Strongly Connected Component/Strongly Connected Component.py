import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
re_graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    re_graph[b].append(a)

visited = [False]*(v+1)
finish_order = []

def first_dfs(node):
    visited[node] = True
    for nxt in graph[node]:
        if visited[nxt]:
            continue
        first_dfs(nxt)

    finish_order.append(node)

for node in range(1, v+1):
    if not visited[node]:
        first_dfs(node)

visited = [False]*(v+1)
scc_list = []

def second_dfs(node, component):
    visited[node] = True
    component.append(node)

    for nxt in re_graph[node]:
        if visited[nxt]:
            continue

        second_dfs(nxt, component)

for node in reversed(finish_order):
    if visited[node]:
        continue

    component = []
    second_dfs(node, component)
    component.sort()
    scc_list.append(component)

scc_list.sort(key=lambda component: component[0])

ans = []
ans.append(str(len(scc_list)))

for component in scc_list:
    line = []

    for node in component:
        line.append(str(node))

    line.append("-1")
    ans.append(' '.join(line))

print('\n'.join(ans))