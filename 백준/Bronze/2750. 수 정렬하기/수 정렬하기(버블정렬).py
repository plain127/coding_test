import sys
N = int(sys.stdin.readline())
arr=[]
for i in range(N):
    arr.append(int(sys.stdin.readline()))

def bubble_sort(A):
    n = len(A)
    for i in range(n-1,0,-1):
        bChanged = False
        for j in range(i):
            if(A[j]>A[j+1]):
                A[j],A[j+1]=A[j+1],A[j]
                bChanged = True
        
        if not bChanged:
            break

bubble_sort(arr)
for i in arr:
    print(i)
