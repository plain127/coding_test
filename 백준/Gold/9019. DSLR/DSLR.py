import sys
from collections import deque

input = sys.stdin.readline

def solve_case(A, B):
    if A == B:
        return ""  # 이미 같은 경우

    visited = [False] * 10000
    parent = [-1] * 10000   # 이전 정점
    how = [''] * 10000      # 이전에서 여기로 올 때 사용한 연산 문자

    q = deque([A])
    visited[A] = True

    while q:
        x = q.popleft()

        # D
        nx = (x * 2) % 10000
        if not visited[nx]:
            visited[nx] = True
            parent[nx] = x
            how[nx] = 'D'
            if nx == B:
                break
            q.append(nx)

        # S
        nx = x - 1 if x > 0 else 9999
        if not visited[nx]:
            visited[nx] = True
            parent[nx] = x
            how[nx] = 'S'
            if nx == B:
                break
            q.append(nx)

        # L
        nx = (x % 1000) * 10 + (x // 1000)
        if not visited[nx]:
            visited[nx] = True
            parent[nx] = x
            how[nx] = 'L'
            if nx == B:
                break
            q.append(nx)

        # R
        nx = (x % 10) * 1000 + (x // 10)
        if not visited[nx]:
            visited[nx] = True
            parent[nx] = x
            how[nx] = 'R'
            if nx == B:
                break
            q.append(nx)

    # 명령 복원
    path = []
    cur = B
    while cur != A:
        path.append(how[cur])
        cur = parent[cur]
    path.reverse()
    return ''.join(path)

def main():
    t = int(input())
    out_lines = []
    for _ in range(t):
        A, B = map(int, input().split())
        out_lines.append(solve_case(A, B))
    print('\n'.join(out_lines))

if __name__ == "__main__":
    main()