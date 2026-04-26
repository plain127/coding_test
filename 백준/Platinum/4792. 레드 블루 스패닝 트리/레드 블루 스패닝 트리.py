import sys

input = sys.stdin.readline


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


def count_blue(n, edges):
    parent = list(range(n + 1))
    blue_count = 0
    used = 0

    for color, a, b in edges:
        if union(parent, a, b):
            used += 1

            if color == 'B':
                blue_count += 1

            if used == n - 1:
                break

    return blue_count


answers = []

while True:
    n, m, k = map(int, input().split())

    if n == 0 and m == 0 and k == 0:
        break

    edges = []

    for _ in range(m):
        color, a, b = input().split()
        edges.append((color, int(a), int(b)))

    red_first = sorted(edges, key=lambda x: 0 if x[0] == 'R' else 1)
    min_blue = count_blue(n, red_first)

    blue_first = sorted(edges, key=lambda x: 0 if x[0] == 'B' else 1)
    max_blue = count_blue(n, blue_first)

    if min_blue <= k <= max_blue:
        answers.append('1')
    else:
        answers.append('0')

sys.stdout.write('\n'.join(answers))