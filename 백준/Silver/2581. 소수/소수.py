M=int(input())
N=int(input())
if(M<=N and N<=10000):
    arr=[]
    for i in range(M,N+1):
        j=2
        if(i==2):
            arr.append(i)
        while(j<i):
            if(i%j==0):
                break
            j+=1
            if(j==i):
                arr.append(i)
    if(not arr):
        print(-1)
    else:
        print(sum(arr))
        print(min(arr))    