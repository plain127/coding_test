def cal(i):
    n=i*(i+1)/2
    return n

X=int(input())
i=1
if(1<=X and X<=10000000):
    while(1):
        if(cal(i-1)<=X and X<=cal(i)):
            break
        i+=1
    if(i%2==0):
        cnt=cal(i)-X
        a=int(i-cnt)
        b=int(cnt+1)
    elif(i%2!=0):
        cnt=cal(i)-X
        a=int(cnt+1)
        b=int(i-cnt)
    print(a,b,sep='/')