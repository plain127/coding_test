import sys
input = sys.stdin.readline

arr = []

for i in range(5):
    arr.append(input())
avg=0
for i in range(5):
    avg+=int(arr[i])
avg//=5

arr.sort()

num=len(arr)//2

print(avg)
print(arr[num])
