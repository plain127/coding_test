import sys

input = sys.stdin.readline

n = int(input())
MOD = 1000000007

def mat_mul(a, b):
    return [
        [
            (a[0][0]*b[0][0] + a[0][1]*b[1][0])%MOD,
            (a[0][0]*b[0][1] + a[0][1]*b[1][1])%MOD
        ],
        [
            (a[1][0]*b[0][0] + a[1][1]*b[1][0])%MOD,
            (a[1][0]*b[0][1] + a[1][1]*b[1][1])%MOD
        ]
    ] 

def mat_pow(mat, exp):
    if exp == 1:
        return mat

    half = mat_pow(mat, exp//2)

    if exp%2 == 0:
        return mat_mul(half, half)
    else:
        return mat_mul(mat_mul(half, half), mat)
        
if n == 0:
    print(0)
else:
    base = [[1,1],[1,0]]
    ans = mat_pow(base, n)
    print(ans[0][1])