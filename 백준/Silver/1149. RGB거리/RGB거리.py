import sys

input = sys.stdin.readline

n = int(input())
price = [list(map(int, input().split())) for _ in range(n)]

for i in range(1,n):
    price[i][0] = min(price[i-1][1], price[i-1][2]) + price[i][0]
    price[i][1] = min(price[i-1][0], price[i-1][2]) + price[i][1]
    price[i][2] = min(price[i-1][0], price[i-1][1]) + price[i][2]

print(min(price[n-1]))
