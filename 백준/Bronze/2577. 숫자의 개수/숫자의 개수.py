A = int(input())
B = int(input())
C = int(input())
D = A*B*C
num = []
count = 1
while(1):
    m1 = D%10
    D = (D-m1)/10
    num.append(m1)
    if(D==0):
        break
for i in range(0,10):
    cnt = num.count(i)
    print(cnt)