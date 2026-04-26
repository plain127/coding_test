import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

answer = []

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    parent = [i for i in range(n + 1)]
    diff = [0] * (n + 1)
    size = [1] * (n + 1)

    def find(x):
        if parent[x] == x:
            return x

        old_parent = parent[x]
        root = find(old_parent)
        diff[x] += diff[old_parent]
        parent[x] = root

        return root

    def union(a, b, w):
        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            return

        if size[root_a] < size[root_b]:
            parent[root_a] = root_b
            diff[root_a] = diff[b] - diff[a] - w
            size[root_b] += size[root_a]
        else:
            parent[root_b] = root_a
            diff[root_b] = w + diff[a] - diff[b]
            size[root_a] += size[root_b]

    for _ in range(m):
        data = input().split()
        command = data[0]

        if command == '!':
            a = int(data[1])
            b = int(data[2])
            w = int(data[3])

            union(a, b, w)
        else:
            a = int(data[1])
            b = int(data[2])

            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                answer.append('UNKNOWN')
            else:
                answer.append(str(diff[b] - diff[a]))

print('\n'.join(answer))