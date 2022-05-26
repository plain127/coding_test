N=int(input())
count=0
if(N>=0 and N<=99):
    if(N<10):
        N*=10
    a=N
    while True:
        add_val=a//10+a%10
        result=(a%10)*10+add_val%10
        a = result
        count+=1;
        if(result== N):
            break
print(count)