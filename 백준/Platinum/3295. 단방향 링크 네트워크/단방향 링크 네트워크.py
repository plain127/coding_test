import sys
from collections import deque

input = sys.stdin.buffer.readline
INF = 10 ** 9


def hopcroft_karp(graph, n):
    pair_left = [-1] * n
    pair_right = [-1] * n
    dist = [0] * n

    def bfs():
        q = deque()
        found = False

        for left in range(n):
            if pair_left[left] == -1:
                dist[left] = 0
                q.append(left)
            else:
                dist[left] = INF

        while q:
            left = q.popleft()

            for right in graph[left]:
                next_left = pair_right[right]

                if next_left == -1:
                    found = True
                elif dist[next_left] == INF:
                    dist[next_left] = dist[left] + 1
                    q.append(next_left)

        return found

    def dfs(left):
        for right in graph[left]:
            next_left = pair_right[right]

            if next_left == -1 or (
                dist[next_left] == dist[left] + 1 and dfs(next_left)
            ):
                pair_left[left] = right
                pair_right[right] = left
                return True

        dist[left] = INF
        return False

    matching = 0

    while bfs():
        for left in range(n):
            if pair_left[left] == -1:
                if dfs(left):
                    matching += 1

    return matching


t = int(input())
answers = []

for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    answers.append(str(hopcroft_karp(graph, n)))

sys.stdout.write('\n'.join(answers))