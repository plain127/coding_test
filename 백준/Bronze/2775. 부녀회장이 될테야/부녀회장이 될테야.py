T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    if(k>=1 and n<=14):
        count1 = []
        count2 = []
        for i in range(n):
            count2.append(i+1)
        count1.append(count2)
        for i in range(k-1):
            count3 = []
            count1.append(count3)
        for i in range(1,k):
            count1[i].append(1)
        i=1
        while(i!=k): 
            j=1
            while(j!=n):
                a = count1[i][j-1]
                b = count1[i-1][j]
                count1[i].append(a+b)
                j+=1
            i+=1
        result=0
        for i in range(n):
            result+=count1[k-1][i]
        print(result)