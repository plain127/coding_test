import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    graph = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((e, s, -t))

    dist = [0]*(n+1)
    has_cycle = False

    for i in range(1, n+1):
        updated = False

        for cur, nxt, cost in graph:
            if dist[nxt] > dist[cur]+cost:
                dist[nxt] = dist[cur]+cost
                updated = True

                if i == n:
                    has_cycle = True
                    break
        
        if has_cycle:
            break

        if not updated:
            break
    
    print('YES' if has_cycle else 'NO')