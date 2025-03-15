import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memo = {}

for _ in range(n):
    site, password = map(str, input().strip().split())
    memo[site] = password

results = []
for _ in range(m):
    search = input().strip()
    password = memo[search]
    results.append(password)

for result in results:
    print(result)