import sys
input = sys.stdin.readline

arr = [list(input().rstrip()) for i in range(5)]
length = []

for i in range(5):
    length.append(len(arr[i]))

num = max(length)


for col in range(num):
   for row in range(5):
        try:
           print(arr[row][col],end="")
        except:
           pass