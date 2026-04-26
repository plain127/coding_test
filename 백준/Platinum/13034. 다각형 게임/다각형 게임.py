import sys 

input = sys.stdin.readline  

n = int(input())  
grundy = [0] * (n + 1)  

for size in range(2, n + 1):  
    seen = set() 

    for left in range(size - 1): 
        right = size - 2 - left  

        next_value = grundy[left] ^ grundy[right] 
        seen.add(next_value)

    mex = 0  

    while mex in seen: 
        mex += 1  

    grundy[size] = mex 

if grundy[n] != 0: 
    print(1)  
else:  
    print(2)