import sys

input = sys.stdin.buffer.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

edge_u = [0] * n
edge_v = [0] * n
edge_w = [0] * n

for i in range(1, n):
    u, v, w = map(int, input().split())

    graph[u].append((v, w, i))
    graph[v].append((u, w, i))

    edge_u[i] = u
    edge_v[i] = v
    edge_w[i] = w


parent = [0] * (n + 1)
depth = [0] * (n + 1)
size = [1] * (n + 1)
heavy = [0] * (n + 1)
value_to_parent = [0] * (n + 1)

order = [1]
parent[1] = -1

for x in order:
    for nxt, w, idx in graph[x]:
        if nxt == parent[x]:
            continue

        parent[nxt] = x
        depth[nxt] = depth[x] + 1
        value_to_parent[nxt] = w
        order.append(nxt)

for x in reversed(order):
    max_size = 0

    for nxt, w, idx in graph[x]:
        if parent[nxt] != x:
            continue

        size[x] += size[nxt]

        if size[nxt] > max_size:
            max_size = size[nxt]
            heavy[x] = nxt


head = [0] * (n + 1)
pos = [0] * (n + 1)
base = [0] * n

cur_pos = 0
stack = [(1, 1)]

while stack:
    x, chain_head = stack.pop()

    while x:
        head[x] = chain_head
        pos[x] = cur_pos
        base[cur_pos] = value_to_parent[x]
        cur_pos += 1

        for nxt, w, idx in graph[x]:
            if parent[nxt] == x and nxt != heavy[x]:
                stack.append((nxt, nxt))

        x = heavy[x]


seg_size = 1
while seg_size < n:
    seg_size <<= 1

seg = [0] * (seg_size * 2)

for i in range(n):
    seg[seg_size + i] = base[i]

for i in range(seg_size - 1, 0, -1):
    seg[i] = max(seg[i * 2], seg[i * 2 + 1])


def update(index, value):
    index += seg_size
    seg[index] = value

    index >>= 1
    while index:
        seg[index] = max(seg[index * 2], seg[index * 2 + 1])
        index >>= 1


def query(left, right):
    if left > right:
        return 0

    left += seg_size
    right += seg_size
    result = 0

    while left <= right:
        if left & 1:
            result = max(result, seg[left])
            left += 1

        if not (right & 1):
            result = max(result, seg[right])
            right -= 1

        left >>= 1
        right >>= 1

    return result


def path_query(u, v):
    result = 0

    while head[u] != head[v]:
        if depth[head[u]] < depth[head[v]]:
            u, v = v, u

        result = max(result, query(pos[head[u]], pos[u]))
        u = parent[head[u]]

    if u == v:
        return result

    if depth[u] > depth[v]:
        u, v = v, u

    result = max(result, query(pos[u] + 1, pos[v]))

    return result


edge_pos = [0] * n

for i in range(1, n):
    u = edge_u[i]
    v = edge_v[i]

    if parent[u] == v:
        edge_pos[i] = pos[u]
    else:
        edge_pos[i] = pos[v]


m = int(input())
answer = []

for _ in range(m):
    q, a, b = map(int, input().split())

    if q == 1:
        edge_index = a
        new_cost = b
        update(edge_pos[edge_index], new_cost)
    else:
        u = a
        v = b
        answer.append(str(path_query(u, v)))

print('\n'.join(answer))