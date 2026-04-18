import sys

input = sys.stdin.readline

n = int(input())
liq = list(map(int, input().split()))

left, right = 0, n-1
neut = float('inf')
ak, ac = liq[left], liq[right]

while left < right:
    ne = liq[left] + liq[right]

    if abs(ne) <= neut:
        neut = abs(ne)
        ak, ac = liq[left], liq[right]
    
    if ne < 0:
        left += 1
    else:
        right -= 1

print(ak, ac)