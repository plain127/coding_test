#내 풀이
s = input()

result = 1
for i in s:
    if int(i) == 0:
        continue
    elif int(i) == 1:
        result += 1
    else:
        result*=int(i)
        
print(result)

#책 풀이
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        
print(result)