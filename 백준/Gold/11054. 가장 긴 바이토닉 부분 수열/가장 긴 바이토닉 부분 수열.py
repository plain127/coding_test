import sys

input = sys.stdin.readline

a = int(input())
seq = list(map(int, input().split()))

lis = [1]*1000
lds = [1]*1000

for i in range(a):
    for j in range(i):
        if seq[j] < seq[i]:
            lis[i] = max(lis[i], lis[j]+1)

for i in range(a-1,-1,-1):
    for j in range(a-1,i,-1):
        if seq[j] < seq[i]:
            lds[i] = max(lds[i], lds[j]+1)

print(max(lis[i]+lds[i]-1 for i in range(a)))