
n = int(input())
al = []

for _ in range(n):
    al.append(input())
al = list(set(al))
al.sort()
al.sort(key = lambda x:len(x))

for i in al:
    print(i)