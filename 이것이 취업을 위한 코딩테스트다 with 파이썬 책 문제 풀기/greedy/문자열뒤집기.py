#내가 푼 풀이 
s = input()
count = 0

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] != s[0] :
            count += 1

print(count)

#책 풀이
data = input()
count0 = 0
count1 = 1

if data[0] == '1':
    count0 += 1
else:
    count1 += 1
    
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1
            
print(min(count0, count1))