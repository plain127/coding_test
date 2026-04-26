import sys

input = sys.stdin.buffer.readline


def make_dsu(size):
    return list(range(size + 1))


def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(parent, a, b):
    ra = find(parent, a)
    rb = find(parent, b)

    if ra == rb:
        return False

    parent[rb] = ra
    return True


def bit_add(index, value):
    while index <= n:
        bit[index] += value
        index += index & -index


def bit_sum(index):
    total = 0

    while index > 0:
        total += bit[index]
        index -= index & -index

    return total


def bit_range_sum(left, right):
    return bit_sum(right) - bit_sum(left - 1)


def path_sum(a, b):
    result = 0

    while head[a] != head[b]:
        if depth[head[a]] < depth[head[b]]:
            a, b = b, a

        result += bit_range_sum(pos[head[a]], pos[a])
        a = parent_tree[head[a]]

    if depth[a] > depth[b]:
        a, b = b, a

    result += bit_range_sum(pos[a], pos[b])

    return result


n = int(input())
penguins = [0] + list(map(int, input().split()))

q = int(input())

commands = []
build_parent = make_dsu(n)
final_edges = []

for _ in range(q):
    parts = input().split()
    command = parts[0].decode()
    a = int(parts[1])
    b = int(parts[2])

    commands.append((command, a, b))

    if command == 'bridge':
        if union(build_parent, a, b):
            final_edges.append((a, b))


graph = [[] for _ in range(n + 1)]

for a, b in final_edges:
    graph[a].append(b)
    graph[b].append(a)


parent_tree = [0] * (n + 1)
depth = [0] * (n + 1)
size = [0] * (n + 1)
heavy = [0] * (n + 1)
head = [0] * (n + 1)
pos = [0] * (n + 1)


visited = [False] * (n + 1)

for root in range(1, n + 1):
    if visited[root]:
        continue

    visited[root] = True
    parent_tree[root] = 0
    depth[root] = 0

    stack = [(root, 0, 0)]

    while stack:
        node, parent, state = stack.pop()

        if state == 0:
            stack.append((node, parent, 1))

            for nxt in graph[node]:
                if nxt == parent:
                    continue

                visited[nxt] = True
                parent_tree[nxt] = node
                depth[nxt] = depth[node] + 1
                stack.append((nxt, node, 0))

        else:
            size[node] = 1
            max_child_size = 0

            for nxt in graph[node]:
                if nxt == parent_tree[node]:
                    continue

                size[node] += size[nxt]

                if size[nxt] > max_child_size:
                    max_child_size = size[nxt]
                    heavy[node] = nxt


timer = 0

for root in range(1, n + 1):
    if pos[root] != 0:
        continue

    stack = [(root, root)]

    while stack:
        node, chain_head = stack.pop()

        cur = node

        while cur != 0:
            timer += 1
            pos[cur] = timer
            head[cur] = chain_head

            for nxt in graph[cur]:
                if nxt == parent_tree[cur] or nxt == heavy[cur]:
                    continue

                stack.append((nxt, nxt))

            cur = heavy[cur]


bit = [0] * (n + 1)
current_value = penguins[:]

for island in range(1, n + 1):
    bit_add(pos[island], current_value[island])


live_parent = make_dsu(n)
answer = []

for command, a, b in commands:
    if command == 'bridge':
        if union(live_parent, a, b):
            answer.append('yes')
        else:
            answer.append('no')

    elif command == 'penguins':
        island = a
        new_value = b

        diff = new_value - current_value[island]
        current_value[island] = new_value

        bit_add(pos[island], diff)

    else:
        if find(live_parent, a) != find(live_parent, b):
            answer.append('impossible')
        else:
            answer.append(str(path_sum(a, b)))

sys.stdout.write('\n'.join(answer))