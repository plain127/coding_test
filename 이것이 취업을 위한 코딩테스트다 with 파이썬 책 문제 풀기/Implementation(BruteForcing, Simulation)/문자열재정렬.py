#내 풀이
s = input()
l = []
m = []
for ss in s:
    if ss.isdigit():
        m.append(int(ss))
    else:
        l.append(ord(ss))
            
l.sort()

n = ''

for ls in l:
    n+=chr(ls)

num = 0
for ms in m:
    num+=ms

n+=str(num)
print(n)

#책 풀이
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))
    
print(''.join(result))