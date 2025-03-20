import sys

input = sys.stdin.readline

n = int(input().strip())
coord = list(map(int, input().strip().split()))

sort_coords = sorted(set(coord))

compress = {val : i for i, val in enumerate(sort_coords)}

compress_coord = [compress[val] for val in coord]

print(' '.join(map(str, compress_coord)))