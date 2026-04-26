import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = [0]*(v+1)
bridges = []
visit_count = 0

def dfs(node, parent):
    global visit_count

    visit_count += 1
    order[node] = visit_count

    low = order[node]

    for next_node in graph[node]:
        if next_node == parent:
            continue

        if order[next_node] == 0:
            child_low = dfs(next_node, node)
            low = min(low, child_low)

            if child_low > order[node]:
                bridges.append((min(node, next_node), max(node, next_node)))
        else:
            low = min(low, order[next_node])

    return low

dfs(1, 0)

bridges.sort()
print(len(bridges))

for a, b in bridges:
    print(a, b)
