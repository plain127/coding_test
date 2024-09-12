n = int(input())

count = []
i = 0
while n > 2:
    if n%5 == 0 :
        a = n//5
        if i%3 == 0:
            count.append(a+(i//3))
    elif n%3 == 0:
        a = n//3
        if i%5 == 0:
            count.append(a+(i//5))
    n-=1
    i+=1

if len(count) == 0:
    print(-1)
else:
    print(min(count))