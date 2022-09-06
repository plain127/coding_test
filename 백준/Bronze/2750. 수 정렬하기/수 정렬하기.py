N=int(input())
if N >= 1 and N <= 1000:
    n = list(0 for i in range(0,N))
    for i in range(N):
        n[i] = int(input())
    for i in range(1,N):
        key = n[i]
        while(i > 0 and n[i-1]>n[i]):
            n[i] = n[i-1]
            n[i-1] = key
            i-=1
for i in range(N):
    print(n[i])