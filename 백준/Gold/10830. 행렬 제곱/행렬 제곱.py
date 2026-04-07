import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def multiply(x, y):
    result = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            val = 0
            for k in range(N):
                val += x[i][k] * y[k][j]
            result[i][j] = val % 1000
    
    return result

def power(matrix, exp):
    if exp == 1:
        return [[matrix[i][j] % 1000 for j in range(N)] for i in range(N)]
    
    half = power(matrix, exp // 2)
    half_squared = multiply(half, half)
    
    if exp % 2 == 0:
        return half_squared
    else:
        return multiply(half_squared, matrix)

answer = power(A, B)

for row in answer:
    print(*row)