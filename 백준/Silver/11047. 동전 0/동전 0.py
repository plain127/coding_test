import sys

n, k = map(int,input().split())

value = []
count = 0

for i in range(n):
    value.append(int(sys.stdin.readline()))

i = n - 1 

while k > 0:
    if (k // value[i]) > 0:
        count += k // value[i]
        k = k % value[i]
        i -= 1
        if i < 0 :
            break
    else:
        i -= 1
        if i < 0 :
            break   
        
print(count)