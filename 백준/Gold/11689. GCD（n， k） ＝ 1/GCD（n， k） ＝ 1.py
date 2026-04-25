import sys

input = sys.stdin.readline

n = int(input())

ans = n
x= n

if x%2 == 0:
    ans -= ans//2

    while x%2 == 0:
        x //= 2

p = 3

while p*p <= x:
    if x%p == 0:
        ans -= ans//p
    
        while x%p == 0:
            x //= p

    p += 2

if x > 1:
    ans -= ans // x

print(ans)