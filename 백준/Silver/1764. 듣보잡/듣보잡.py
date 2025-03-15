import sys

input = sys.stdin.readline

n, m = map(int, input().split())
listen = set()
see = set()

for _ in range(n):
    listen.add(input().strip())

for _ in range(m):
    see.add(input().strip())

see_and_listen = sorted(listen.intersection(see))

print(len(see_and_listen))
for i in see_and_listen:
    print(i)