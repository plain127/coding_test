import sys 

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [False]*(n+1)

def backtracking():
    if len(graph) == m:
        print(' '.join(map(str, graph)))
        return 
    
    for i in range(1,n+1):
        if visited[i]:
            continue

        visited[i] = True
        graph.append(i)
        backtracking()
        graph.pop()
        visited[i] = False

backtracking()