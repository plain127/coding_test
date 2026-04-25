import sys

input = sys.stdin.readline

t = input().rstrip('\n')
p = input().rstrip('\n')

n = len(t)
m = len(p)

pi = [0]*m

j = 0

for i in range(1,m):
    while j > 0 and p[i] != p[j]:
        j = pi[j-1]
    
    if p[i] == p[j]:
        j += 1
        pi[i] = j

positions = []

j = 0

for i in range(n):
    while j > 0 and t[i] != p[j]:
        j = pi[j-1]
    
    if t[i] == p[j]:
        if j == m-1:
            positions.append(i-m+2)
            j = pi[j]
        else:
            j += 1

print(len(positions))
print(*positions)