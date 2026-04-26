import sys
from collections import deque

INF = 10 ** 15


class Edge:
    def __init__(self, to, rev, cap, cost):
        self.to = to
        self.rev = rev
        self.cap = cap
        self.cost = cost


def add_edge(graph, fr, to, cap, cost):
    graph[fr].append(Edge(to, len(graph[to]), cap, cost))
    graph[to].append(Edge(fr, len(graph[fr]) - 1, 0, -cost))


def node_in(x):
    return x * 2


def node_out(x):
    return x * 2 + 1


def min_cost_two_flow(graph, node_count, source, sink):
    total_cost = 0
    total_flow = 0

    while total_flow < 2:
        dist = [INF] * node_count
        prev_node = [-1] * node_count
        prev_edge = [-1] * node_count
        in_queue = [False] * node_count

        dist[source] = 0
        q = deque([source])
        in_queue[source] = True

        while q:
            cur = q.popleft()
            in_queue[cur] = False

            for edge_index, edge in enumerate(graph[cur]):
                if edge.cap <= 0:
                    continue

                nxt = edge.to
                next_cost = dist[cur] + edge.cost

                if dist[nxt] > next_cost:
                    dist[nxt] = next_cost
                    prev_node[nxt] = cur
                    prev_edge[nxt] = edge_index

                    if not in_queue[nxt]:
                        q.append(nxt)
                        in_queue[nxt] = True

        if prev_node[sink] == -1:
            break

        flow = 2 - total_flow
        cur = sink

        while cur != source:
            before = prev_node[cur]
            edge_index = prev_edge[cur]
            edge = graph[before][edge_index]
            flow = min(flow, edge.cap)
            cur = before

        cur = sink

        while cur != source:
            before = prev_node[cur]
            edge_index = prev_edge[cur]
            edge = graph[before][edge_index]

            edge.cap -= flow
            graph[cur][edge.rev].cap += flow
            total_cost += flow * edge.cost

            cur = before

        total_flow += flow

    return total_cost


data = list(map(int, sys.stdin.buffer.read().split()))
idx = 0
answers = []

while idx < len(data):
    v = data[idx]
    e = data[idx + 1]
    idx += 2

    node_count = (v + 1) * 2 + 2
    graph = [[] for _ in range(node_count)]

    for city in range(1, v + 1):
        cap = 2 if city == 1 or city == v else 1
        add_edge(graph, node_in(city), node_out(city), cap, 0)

    for _ in range(e):
        a = data[idx]
        b = data[idx + 1]
        c = data[idx + 2]
        idx += 3

        add_edge(graph, node_out(a), node_in(b), 1, c)

    source = node_out(1)
    sink = node_in(v)

    answers.append(str(min_cost_two_flow(graph, node_count, source, sink)))

sys.stdout.write('\n'.join(answers))