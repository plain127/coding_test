def hanoi(n,a,b,c):
    if n==1:
        print('%s %s'%(a,c))
    else:
        hanoi(n-1,a,c,b)
        print('%s %s'%(a,c))
        hanoi(n-1,b,a,c)

def hanoi_num(n):
    if n==1:
        count=1
    else:
        count = hanoi_num(n-1)
        count+=1
        count+=hanoi_num(n-1)
    return count
        
N=int(input())
if N<=20 and N>=1:
    print(hanoi_num(N))
    hanoi(N,'1','2','3')