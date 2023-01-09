import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    n = int(sys.stdin.readline())
    arr.append(n)

def selection_sort(A):
    n=len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1,n):
            if(A[j]<A[least]):
                least = j
        A[i],A[least] = A[least],A[i]

selection_sort(arr)

for i in arr:
    print(i)