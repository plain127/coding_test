import sys
N = int(sys.stdin.readline())
arr=[]
for i in range(N):
    arr.append(int(sys.stdin.readline()))

def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            j-=1
        A[j+1] = key

insertion_sort(arr)
for i in arr:
    print(i)
