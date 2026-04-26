import sys

input = sys.stdin.buffer.readline

INF = 10 ** 9

n, k = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

removed = [False] * n
sub_size = [0] * n
answer = INF

best_dist = [INF] * (k + 1)


def collect_component(start):
    nodes = []
    parent = [-1]

    stack = [(start, -1, 0)]

    while stack:
        node, par, state = stack.pop()

        if state == 0:
            nodes.append(node)
            stack.append((node, par, 1))

            for nxt, _ in graph[node]:
                if nxt == par or removed[nxt]:
                    continue

                stack.append((nxt, node, 0))

        else:
            size = 1

            for nxt, _ in graph[node]:
                if nxt == par or removed[nxt]:
                    continue

                size += sub_size[nxt]

            sub_size[node] = size

    return nodes


def get_centroid(start):
    nodes = collect_component(start)
    total = len(nodes)

    centroid = start
    par = -1
    changed = True

    while changed:
        changed = False

        for nxt, _ in graph[centroid]:
            if nxt == par or removed[nxt]:
                continue

            if sub_size[nxt] > total // 2:
                par = centroid
                centroid = nxt
                changed = True
                break

    return centroid, total


def collect_distances(start, parent, initial_dist, initial_edges):
    result = []
    stack = [(start, parent, initial_dist, initial_edges)]

    while stack:
        node, par, dist, edges = stack.pop()

        if dist > k:
            continue

        result.append((dist, edges))

        for nxt, weight in graph[node]:
            if nxt == par or removed[nxt]:
                continue

            stack.append((nxt, node, dist + weight, edges + 1))

    return result


def decompose(start):
    global answer

    centroid, _ = get_centroid(start)
    removed[centroid] = True

    touched = [0]
    best_dist[0] = 0

    for child, weight in graph[centroid]:
        if removed[child]:
            continue

        distances = collect_distances(child, centroid, weight, 1)

        for dist, edges in distances:
            need = k - dist

            if need < 0:
                continue

            if best_dist[need] != INF:
                candidate = edges + best_dist[need]

                if candidate < answer:
                    answer = candidate

        for dist, edges in distances:
            if edges < best_dist[dist]:
                if best_dist[dist] == INF:
                    touched.append(dist)

                best_dist[dist] = edges

    for dist in touched:
        best_dist[dist] = INF

    for child, _ in graph[centroid]:
        if not removed[child]:
            decompose(child)


sys.setrecursionlimit(10 ** 7)

decompose(0)

print(answer if answer != INF else -1)