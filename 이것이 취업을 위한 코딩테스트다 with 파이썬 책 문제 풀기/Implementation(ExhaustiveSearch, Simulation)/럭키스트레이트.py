#내 풀이
n = input()

num = len(n)//2

first = 0
second = 0

for idx, m in enumerate(n):
    if idx < num:
        first += int(m)
    else:
        second += int(m)

if first == second :
    print('LUCKY')
else:
    print('READY')
    
#책 풀이
n = input()
length = len(n)
summary = 0

for i in range(length//2):
    summary += int(n[i])
    
for i in range(length//2, length):
    summary -= int(n[i])
    
if summary == 0:
    print('LUCKY')
else:
    print('READY')