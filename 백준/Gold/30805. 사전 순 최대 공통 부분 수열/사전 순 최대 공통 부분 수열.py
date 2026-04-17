import sys

input = sys.stdin.readline

n = int(input())
seq_a = list(map(int, input().split()))
m = int(input())
seq_b = list(map(int, input().split()))

i, j = 0, 0
seq = []

while i < n and j < m:
    found = False
    
    for num in range(100,0,-1):
        ai = -1

        for x in range(i,n):
            if seq_a[x] == num:
                ai = x
                break

        if ai == -1:
            continue

        bj = -1

        for y in range(j, m):
            if seq_b[y] == num:
                bj = y
                break

        if bj == -1:
            continue

        seq.append(num)
        i, j = ai+1, bj+1
        found = True
        break

    if not found:
        break

print(len(seq))
if seq:
    print(*seq)
