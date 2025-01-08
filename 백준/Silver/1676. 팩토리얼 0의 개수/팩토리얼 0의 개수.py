import sys

input = sys.stdin.readline

n = int(input())

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n*fact(n-1)

num = fact(n)
num = str(num)
num = num[::-1]

count = 0
for i in num:
    if i == '0':
        count += 1
    else:
        break
print(count)