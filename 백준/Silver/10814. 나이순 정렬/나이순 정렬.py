import sys
input = sys.stdin.readline

n = int(input())

name_age = []
for _ in range(n):
    age, name = input().split()
    name_age.append((int(age), name))

name_age.sort(key=lambda name_age:name_age[0])

for i in name_age:
    age = i[0]
    name = i[1]
    print(str(age)+' '+name)