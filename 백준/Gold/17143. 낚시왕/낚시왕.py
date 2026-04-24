import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())

board = [[None]*C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    board[r][c] = (s, d, z)

def move_axis(pos, speed, dir, lim, pos_dir, neg_dir):
    period = 2*(lim-1)

    if dir == pos_dir:
        x = pos+speed
    else:
        x = (period-pos)+speed
    
    x %= period

    if x < lim:
        return x, pos_dir
    
    return period-x, neg_dir

def move_shark(r, c, s, d, z):
    if d==1 or d==2:
        nr, nd = move_axis(r,s,d,R,2,1)
        return nr, c, s, nd, z
    else:
        nc, nd = move_axis(c,s,d,C,3,4)
        return r, nc, s, nd, z

ans = 0

for fisher_c in range(C):
    for r in range(R):
        if board[r][fisher_c] is not None:
            s, d, z = board[r][fisher_c]
            ans += z
            board[r][fisher_c] = None
            break

    new_board = [[None]*C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if board[r][c] is None:
                continue

            s, d, z = board[r][c]
            nr, nc, ns, nd, nz = move_shark(r,c,s,d,z)

            if new_board[nr][nc] is None:
                new_board[nr][nc] = (ns, nd, nz)
            else:
                old_s, old_d, old_z = new_board[nr][nc]

                if nz > old_z:
                    new_board[nr][nc] = (ns, nd, nz)
    
    board = new_board

print(ans)