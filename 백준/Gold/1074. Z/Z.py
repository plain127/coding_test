import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())

def divide(size, row, col):
    if size == 0:
        return 0

    half = 2**(size-1)

    if row < half and col < half:
        return divide(size-1, row, col)
    elif row < half and col >= half:
        return half*half + divide(size-1, row, col-half)
    elif row >= half and col < half:
        return 2*half*half + divide(size-1,row-half, col)
    else:
        return 3*half*half + divide(size-1,row-half, col-half)


print(divide(n, r, c))