n=int(input())
arrs=[]

for _ in range(n):
  start,end=map(int,input().split())
  arrs.append([start,end])

arrs.sort(key=lambda x:(x[1],x[0]))

temp=arrs[0][1]
count=1

for i in range(1,n):
  if arrs[i][0]>=temp:
    count+=1
    temp=arrs[i][1]
print(count)