n, m = map(int, input().split())
gcd = 1

for i in range(1, n+1):
    if(n%i==0)and(m%i==0):
        gcd = i

a = n//gcd
b = m//gcd

lcm = a*b*gcd 
print(gcd)
print(lcm)  