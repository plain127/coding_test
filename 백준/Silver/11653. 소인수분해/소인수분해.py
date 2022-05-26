N = int(input())
if(1<=N and N<=10000000):
    i = 2
    while(i<=N):
        if(N%i==0):
            N = N//i
            print(i)
        else:
            i+=1