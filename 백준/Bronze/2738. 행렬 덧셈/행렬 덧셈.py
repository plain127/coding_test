import sys
n,m=map(int,sys.stdin.readline().split())
A = []
for row in range(n):
    row = list(map(int,sys.stdin.readline().split()))
    A.append(row)

B = []
for row in range(n):
    row = list(map(int,sys.stdin.readline().split()))
    B.append(row)
      

for row in range(n):
    for col in range(m):
        print(A[row][col]+B[row][col],end=' ')
    print()