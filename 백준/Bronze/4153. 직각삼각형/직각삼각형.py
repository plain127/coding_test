import sys

input = sys.stdin.readline

while True:
    n = list(map(int, input().split()))
    n.sort()
    if n[0]==0 and n[1]==0 and n[2]==0:
        break
    
    if n[2]*n[2] == (n[0]*n[0] + n[1]*n[1]):
        print('right')
    else:
        print('wrong')