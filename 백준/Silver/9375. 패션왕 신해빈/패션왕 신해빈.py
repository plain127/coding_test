import sys

input = sys.stdin.readline

counts = []
for _ in range(int(input())):
    n = int(input())
    type_counts = {}

    for _ in range(n):
        name, kind = input().strip().split()
        if kind in type_counts:
            type_counts[kind] += 1
        else:
            type_counts[kind] = 1
    
    count = 1
    for cnt in type_counts.values():
        count *= (cnt + 1)
    count -= 1

    counts.append(count)

for count in counts:
    print(count)