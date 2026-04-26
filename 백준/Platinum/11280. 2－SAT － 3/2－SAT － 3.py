import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
size = 2*n
graph = [[] for _ in range(size)]
rev = [[] for _ in range(size)]

def idx(x):
    if x > 0:
        return 2*(x-1)

    return 2*(-x-1)+1

def opposite(node):
    return node ^ 1

for _ in range(m):
    a, b = map(int, input().split())

    a_node = idx(a)
    b_node = idx(b)

    graph[opposite(a_node)].append(b_node)
    rev[b_node].append(opposite(a_node))

    graph[opposite(b_node)].append(a_node)
    rev[a_node].append(opposite(b_node))

visited = [False]*size
order = []

def first_dfs(node):
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            first_dfs(next_node)

    order.append(node)

for node in range(size):
    if not visited[node]:
        first_dfs(node)

comp = [-1]*size
comp_id = 0

def second_dfs(node, comp_id):
    comp[node] = comp_id

    for next_node in rev[node]:
        if comp[next_node] == -1:
            second_dfs(next_node, comp_id)

for node in reversed(order):
    if comp[node] != -1:
        continue

    second_dfs(node, comp_id)
    comp_id += 1

for i in range(n):
    true_node = 2*i
    false_node = 2*i + 1

    if comp[true_node] == comp[false_node]:
        print(0)
        sys.exit()

print(1)