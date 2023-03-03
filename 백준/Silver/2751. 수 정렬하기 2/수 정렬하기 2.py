import sys
input = sys.stdin.readline
N= int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))

arr.sort()

for i in range(N):
    print(arr[i])