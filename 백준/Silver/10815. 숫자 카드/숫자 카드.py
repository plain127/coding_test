import sys
N = int(sys.stdin.readline())
arr1 = list(map(int,sys.stdin.readline().split()))
if N == len(arr1):
    M = int(sys.stdin.readline())
    arr2 = list(map(int,sys.stdin.readline().split()))
    if M == len(arr2):
       s1 = set(arr1)
       for i in arr2:
        if i not in s1:
            print(0)
        else:
            print(1)