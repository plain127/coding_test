N=int(input())
s=0
if(N<=1000):
    score =list(map(int,input().split(' ',N)))
M = max(score)
if(M!=0 and M<=100):
    for i in range(0,N):
        s=s+score[i]/M*100
avg=s/N
print(avg)