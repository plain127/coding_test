m, n = map(int, input().split())

prime = [True]*(n+1)
for i in range(2, int((n+1)**0.5)+1):
    if prime[i]:
        for j in range(2*i, n+1, i):
            prime[j] = False

for i in range(m,n+1):
    if i > 1 and prime[i] == True:
        print(i)