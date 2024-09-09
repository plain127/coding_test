n = int(input())

m = 0

for i in range(1,1000000):
    k = n 
    i = str(i)
    for j in i:
        k = k - int(j)
    if k - int(i) == 0:
        m = int(i)
        break

print(m)