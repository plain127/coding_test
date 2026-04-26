import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

INF = 10 ** 9
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

start = None
school = None

for r in range(n):
    for c in range(m):
        if board[r][c] == 'K':
            start = (r, c)
        elif board[r][c] == 'H':
            school = (r, c)

sr, sc = start
hr, hc = school

if abs(sr - hr) + abs(sc - hc) == 1:
    print(-1)
    sys.exit()


def cell_id(r, c):
    return r * m + c


def node_in(r, c):
    return cell_id(r, c) * 2


def node_out(r, c):
    return cell_id(r, c) * 2 + 1


class Edge:
    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap


node_count = n * m * 2
graph = [[] for _ in range(node_count)]


def add_edge(fr, to, cap):
    graph[fr].append(Edge(to, len(graph[to]), cap))
    graph[to].append(Edge(fr, len(graph[fr]) - 1, 0))


for r in range(n):
    for c in range(m):
        if board[r][c] == '#':
            continue

        inn = node_in(r, c)
        out = node_out(r, c)

        if board[r][c] == 'K' or board[r][c] == 'H':
            add_edge(inn, out, INF)
        else:
            add_edge(inn, out, 1)

for r in range(n):
    for c in range(m):
        if board[r][c] == '#':
            continue

        cur_out = node_out(r, c)

        for dr, dc in DIRS:
            nr = r + dr
            nc = c + dc

            if not (0 <= nr < n and 0 <= nc < m):
                continue

            if board[nr][nc] == '#':
                continue

            next_in = node_in(nr, nc)
            add_edge(cur_out, next_in, INF)


source = node_out(sr, sc)
sink = node_in(hr, hc)


def bfs():
    level = [-1] * node_count
    q = deque([source])
    level[source] = 0

    while q:
        cur = q.popleft()

        for edge in graph[cur]:
            if edge.cap > 0 and level[edge.to] == -1:
                level[edge.to] = level[cur] + 1
                q.append(edge.to)

    return level


def dfs(cur, flow, level, work):
    if cur == sink:
        return flow

    while work[cur] < len(graph[cur]):
        edge = graph[cur][work[cur]]

        if edge.cap > 0 and level[edge.to] == level[cur] + 1:
            pushed = dfs(edge.to, min(flow, edge.cap), level, work)

            if pushed > 0:
                edge.cap -= pushed
                graph[edge.to][edge.rev].cap += pushed
                return pushed

        work[cur] += 1

    return 0


answer = 0

while True:
    level = bfs()

    if level[sink] == -1:
        break

    work = [0] * node_count

    while True:
        pushed = dfs(source, INF, level, work)

        if pushed == 0:
            break

        answer += pushed

print(answer)