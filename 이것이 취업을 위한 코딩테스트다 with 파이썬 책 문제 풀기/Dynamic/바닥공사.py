#내 풀이
import sys

input = sys.stdin.readline

n = int(input())

tile = [0]*1001
tile[1] = 1
tile[2] = 3

for i in range(3, n+1):
    tile[i] = tile[i-1] + 2 * tile[i-2]

print(tile[n]%796796)

#책 풀이
n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2*d[i-2])%796796

print(d[n])