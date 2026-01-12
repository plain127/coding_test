import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
x_s = sorted(set(x))

compress = {val : i for i, val in enumerate(x_s)}
compress_x = [compress[val] for val in x]
print(' '.join(map(str, compress_x)))