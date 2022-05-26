A = []
B = []
C = []
D = 10
for i in range(0,10):
    A.append(int(input()))
    B.append(A[i]%42)
for i in range(0,42):
    cnt = B.count(i)
    if(cnt != 0):
        D=D-cnt+1
print(D)