import sys

while True:
    num = sys.stdin.readline().strip()
    
    if num == '0':
        break
    
    n = len(num)//2

    arr1 = num[:n]
    if len(num)%2 == 0:
        arr2 = num[n:]
    else:
        arr2 = num[n+1:]
    
    if arr1 == arr2[::-1]:
        print('yes')
    else:
        print('no')