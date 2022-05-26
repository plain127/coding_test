def cal(i):
    n = 3*i*i-3*i+1
    return n

N=int(input())
i = 1
if(N>=1 and N<=1000000000):
    while(1):
        if(cal(i-1)<=N and  N<=cal(i)):
            print(i)
            break
        i+=1