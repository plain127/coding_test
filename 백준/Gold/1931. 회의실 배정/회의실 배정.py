import sys

input = sys.stdin.readline

n = int(input())
tables = []

for _ in range(n):
    start, end = map(int,input().split())
    tables.append((start, end))

tables.sort(key=lambda x:(x[1], x[0]))

count = 0
end = 0
for table in tables: 
    start, e = table

    if start < end:
        continue

    end = e
    count += 1


print(count)