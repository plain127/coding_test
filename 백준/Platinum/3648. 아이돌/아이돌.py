import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

answers = []

def get_node(x):
    if x > 0:
        return 2 * (x - 1)

    return 2 * (-x - 1) + 1

def opposite(node):
    return node ^ 1

def add_clause(graph, rev, a, b):
    a_node = get_node(a)
    b_node = get_node(b)

    graph[opposite(a_node)].append(b_node)
    rev[b_node].append(opposite(a_node))

    graph[opposite(b_node)].append(a_node)
    rev[a_node].append(opposite(b_node))

def first_dfs(node, graph, visited, order):
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            first_dfs(next_node, graph, visited, order)

    order.append(node)

def second_dfs(node, rev, comp, comp_id):
    comp[node] = comp_id

    for next_node in rev[node]:
        if comp[next_node] == -1:
            second_dfs(next_node, rev, comp, comp_id)

while True:
    line = input()

    if not line:
        break

    n, m = map(int, line.split())
    size = 2 * n

    graph = [[] for _ in range(size)]
    rev = [[] for _ in range(size)]

    for _ in range(m):
        a, b = map(int, input().split())
        add_clause(graph, rev, a, b)

    add_clause(graph, rev, 1, 1)

    visited = [False] * size
    order = []

    for node in range(size):
        if not visited[node]:
            first_dfs(node, graph, visited, order)

    comp = [-1] * size
    comp_id = 0

    for node in reversed(order):
        if comp[node] != -1:
            continue

        second_dfs(node, rev, comp, comp_id)
        comp_id += 1

    possible = True

    for person in range(n):
        true_node = 2 * person

        false_node = 2 * person + 1

        if comp[true_node] == comp[false_node]:
            possible = False
            break

    if possible:
        answers.append('yes')
    else:
        answers.append('no')

print('\n'.join(answers))