import sys
arr = []
for row in range(9):
    row = list(map(int,sys.stdin.readline().split()))
    arr.append(row)

num=0
for row in range(9):
    for col in range(9):
        if num<=arr[row][col]:
            num = arr[row][col]
            a= row+1
            b = col+1
print(num)
print(a, b)