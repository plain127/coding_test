import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

for num in b:
    if num in a:
        print(1)
    else:
        print(0)