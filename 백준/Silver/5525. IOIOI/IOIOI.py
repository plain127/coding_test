import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

count = 0
pattern = 0
curr = 0

while curr < m-1:
    if s[curr] == 'I' and s[curr+1] == 'O' and curr+2<m and s[curr+2] == 'I':
        pattern += 1
        curr += 2
        if pattern == n:
            pattern -= 1
            count += 1
    else:
        pattern = 0
        curr += 1

print(count)