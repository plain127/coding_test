import sys

input = sys.stdin.readline

mod = 1000003

n, s, e, t = map(int, input().split())

s -= 1
e -= 1

size = n * 5

def idx(node, remain):
    return node * 5 + remain

def identity():
    result = [[0] * size for _ in range(size)]

    for i in range(size):
        result[i][i] = 1

    return result

def multiply(a, b):
    result = [[0] * size for _ in range(size)]

    for i in range(size):
        for k in range(size):
            if a[i][k] == 0:
                continue

            for j in range(size):
                if b[k][j] == 0:
                    continue

                result[i][j] += a[i][k] * b[k][j]
                result[i][j] %= mod

    return result


def matrix_power(matrix, power):
    result = identity()

    while power > 0:
        if power % 2 == 1:
            result = multiply(result, matrix)

        matrix = multiply(matrix, matrix)
        power //= 2

    return result

matrix = [[0] * size for _ in range(size)]
road_info = []

for _ in range(n):
    road_info.append(input().strip())

for u in range(n):
    for v in range(n):
        cost = int(road_info[u][v])

        if cost == 0:
            continue

        matrix[idx(u, 0)][idx(v, cost - 1)] = 1

for node in range(n):
    for remain in range(1, 5):
        matrix[idx(node, remain)][idx(node, remain - 1)] = 1

powered = matrix_power(matrix, t)
answer = powered[idx(s, 0)][idx(e, 0)]

print(answer % mod)