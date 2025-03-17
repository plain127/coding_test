import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int,input().split())
path = []
visited = [False]*(n+1)

def backtracking():
    if len(path) == m:
        print(' '.join(map(str, path)))
        return

    for i in range(1,n+1):

        visited[i] = True
        path.append(i)

        backtracking()
        visited[i] = False
        path.pop()


backtracking()