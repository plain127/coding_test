N = int(input())
if(N<=100):
    arr = list(map(int,input().split(" ",N)))
    count = 0
    for i in range(N):
        j = 2
        if(arr[i]==2):
            count+=1
        while(j<arr[i]):
            if(arr[i]%j==0):
                break
            j+=1
            if(j==arr[i]):
                count+=1
print(count)