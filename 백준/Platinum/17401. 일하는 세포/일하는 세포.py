import sys

input = sys.stdin.readline
MOD = 1000000007

t, n, d = map(int, input().split())

def identity():
    result = [[0]*n for _ in range(n)]

    for i in range(n):
        result[i][i] = 1

    return result

def multiply(a, b):
    result = [[0]*n for _ in range(n)]

    for i in range(n):
        for k in range(n):
            if a[i][k] == 0:
                continue

            for j in range(n):
                result[i][j] += a[i][k]*b[k][j]
                result[i][j] %= MOD
    return result

def matrix_power(base, power):
    result = identity()

    while power > 0:
        if power%2 == 1:
            result = multiply(result, base)

        base = multiply(base, base)
        power //= 2
    return result

maps = []
for _ in range(t):
    matrix = [[0]*n for _ in range(n)]
    m = int(input())

    for _ in range(m):
        a, b, c = map(int, input().split())
        matrix[a-1][b-1] = c%MOD

    maps.append(matrix)

period = identity()

for matrix in maps:
    period = multiply(period, matrix)

full_cnt = d//t
rest_cnt = d%t

ans = matrix_power(period, full_cnt)

for i in range(rest_cnt):
    ans = multiply(ans, maps[i])

for row in ans:
    print(' '.join(map(str, row)))