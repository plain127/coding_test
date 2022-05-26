n=int(input())
if(n<abs(1000001)):
        N=list(map(int,input().split(' ',n)))
a=min(N)
b=max(N)
print(a,b)