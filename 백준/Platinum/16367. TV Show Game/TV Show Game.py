import sys

data = sys.stdin.buffer.read().split()

k = int(data[0])       # 램프 개수
n = int(data[1])       # 참가자 수

node_count = 2 * k
graph = [[] for _ in range(node_count)]
reverse_graph = [[] for _ in range(node_count)]


def literal(lamp_token, color_token):
    lamp = int(lamp_token) - 1

    # R을 true, B를 false로 둔다.
    if color_token == b'R':
        return 2 * lamp

    return 2 * lamp + 1


def add_edge(a, b):
    graph[a].append(b)
    reverse_graph[b].append(a)


def add_clause(x, y):
    # (x or y) = not x -> y, not y -> x
    add_edge(x ^ 1, y)
    add_edge(y ^ 1, x)


idx = 2

for _ in range(n):
    a = literal(data[idx], data[idx + 1])
    idx += 2

    b = literal(data[idx], data[idx + 1])
    idx += 2

    c = literal(data[idx], data[idx + 1])
    idx += 2

    # 3개 중 2개 이상 true
    # = (a or b) and (a or c) and (b or c)
    add_clause(a, b)
    add_clause(a, c)
    add_clause(b, c)


# Kosaraju 1단계: 끝나는 순서 order 만들기
visited = [False] * node_count
order = []

for start in range(node_count):
    if visited[start]:
        continue

    visited[start] = True
    stack = [(start, 0)]

    while stack:
        node, edge_index = stack[-1]

        if edge_index < len(graph[node]):
            next_node = graph[node][edge_index]
            stack[-1] = (node, edge_index + 1)

            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node, 0))
        else:
            order.append(node)
            stack.pop()


# Kosaraju 2단계: reverse graph에서 SCC 번호 붙이기
component = [-1] * node_count
component_id = 0

for start in reversed(order):
    if component[start] != -1:
        continue

    component[start] = component_id
    stack = [start]

    while stack:
        node = stack.pop()

        for next_node in reverse_graph[node]:
            if component[next_node] == -1:
                component[next_node] = component_id
                stack.append(next_node)

    component_id += 1


answer = []

for lamp in range(k):
    red = 2 * lamp
    blue = 2 * lamp + 1

    # R과 B가 동시에 강제되면 불가능
    if component[red] == component[blue]:
        print(-1)
        sys.exit()

    # Kosaraju SCC 번호 기준: 더 나중 컴포넌트가 true
    if component[red] > component[blue]:
        answer.append('R')
    else:
        answer.append('B')

print(''.join(answer))