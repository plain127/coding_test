import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]

for edge_id in range(e):
    a, b = map(int, input().split())
    graph[a].append((b, edge_id))
    graph[b].append((a, edge_id))

order = [0]*(v+1)
is_cut = [False]*(v+1)
visit_count = 0

def dfs(node, parent_edge):
    global visit_count

    visit_count += 1
    order[node] = visit_count

    low = order[node]
    child_count = 0

    for next_node, edge_id in graph[node]:
        if edge_id == parent_edge:
            continue
        
        if order[next_node] == 0:
            child_count += 1
            child_low = dfs(next_node, edge_id)
            low = min(low, child_low)

            if parent_edge != -1 and child_low >= order[node]:
                is_cut[node] = True
        else:
            low = min(low, order[next_node])
    
    if parent_edge == -1 and child_count >= 2:
        is_cut[node] = True

    return low

for node in range(1, v+1):
    if order[node] == 0:
        dfs(node, -1)

answer = []

for node in range(1, v+1):
    if is_cut[node]:
        answer.append(node)

print(len(answer))
print(*answer)