import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = []

rr = rc = 0
br = bc = 0

for r in range(n):
    row = list(input().strip())

    for c in range(m):
        if row[c] == 'R':
            rr, rc = r, c
            row[c] = '.'   
        elif row[c] == 'B':
            br, bc = r, c
            row[c] = '.'   

    board.append(row)

dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def roll(r, c, dr, dc):
    move_cnt = 0

    while True:
        nr, nc = r + dr, c + dc

        if board[nr][nc] == '#':
            break

        r, c = nr, nc
        move_cnt += 1

        if board[r][c] == 'O':
            return r, c, move_cnt, True

    return r, c, move_cnt, False


q = deque()
q.append((rr, rc, br, bc, 0))

visited = set()
visited.add((rr, rc, br, bc))

while q:
    rr, rc, br, bc, depth = q.popleft()

    if depth >= 10:
        continue

    for dr, dc in dirs:
        nrr, nrc, r_cnt, r_hole = roll(rr, rc, dr, dc)
        nbr, nbc, b_cnt, b_hole = roll(br, bc, dr, dc)

        if b_hole:
            continue

        if r_hole:
            print(depth + 1)
            sys.exit(0)

        if nrr == nbr and nrc == nbc:
            if r_cnt > b_cnt:
                nrr -= dr
                nrc -= dc
            else:
                nbr -= dr
                nbc -= dc

        state = (nrr, nrc, nbr, nbc)

        if state not in visited:
            visited.add(state)
            q.append((nrr, nrc, nbr, nbc, depth + 1))

print(-1)