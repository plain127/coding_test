N=int(input())
li=[]
if(3<=N and N<=5000):
    a = N//3
    for x in range(a+1):
        b = N-3*x
        if(b%5==0):
            y = b//5
            li.append(x+y)
        elif(b==0):
            y = 0
            li.append(x+y)
        
if(not li):
    print(-1)
else:
    print(min(li))