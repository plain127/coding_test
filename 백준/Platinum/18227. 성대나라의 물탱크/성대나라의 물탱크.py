import sys

input = sys.stdin.buffer.readline

n, root = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

tin = [0] * (n + 1)
tout = [0] * (n + 1)
depth = [0] * (n + 1)

timer = 0
stack = [(root, 0, 1, 0)]

while stack:
    node, parent, dep, state = stack.pop()

    if state == 0:
        timer += 1
        tin[node] = timer
        depth[node] = dep

        stack.append((node, parent, dep, 1))

        for next_node in graph[node]:
            if next_node == parent:
                continue

            stack.append((next_node, node, dep + 1, 0))

    else:
        tout[node] = timer

bit = [0] * (n + 1)


def add(index, value):
    while index <= n:
        bit[index] += value
        index += index & -index


def prefix_sum(index):
    total = 0

    while index > 0:
        total += bit[index]
        index -= index & -index

    return total


def range_sum(left, right):
    return prefix_sum(right) - prefix_sum(left - 1)


q = int(input())
answer = []

for _ in range(q):
    command, city = map(int, input().split())

    if command == 1:
        add(tin[city], 1)

    else:
        count = range_sum(tin[city], tout[city])
        answer.append(str(count * depth[city]))

sys.stdout.write('\n'.join(answer))