import sys

input = sys.stdin.readline

MOD = 1_000_000_007
N = 8

D = int(input())

matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0],  
    [1, 0, 1, 1, 0, 0, 0, 0],  
    [1, 1, 0, 1, 1, 0, 0, 0],  
    [0, 1, 1, 0, 1, 1, 0, 0],  
    [0, 0, 1, 1, 0, 1, 0, 1],  
    [0, 0, 0, 1, 1, 0, 1, 0],  
    [0, 0, 0, 0, 0, 1, 0, 1],  
    [0, 0, 0, 0, 1, 0, 1, 0],  
]

def multiply(a, b):
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for k in range(N):
            if a[i][k] == 0:
                continue

            for j in range(N):
                result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % MOD

    return result

def power(mat, exp):
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        result[i][i] = 1

    while exp > 0:
        if exp % 2 == 1:
            result = multiply(result, mat)

        mat = multiply(mat, mat)

        exp //= 2

    return result

answer = power(matrix, D)
print(answer[0][0])