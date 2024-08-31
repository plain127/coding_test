exps = input()
nums = exps.split('-')


number = []

for num in nums:
    if '+' in num:
        parts = num.split('+')
        sum_value = sum(int(part) for part in parts)
        number.append(sum_value)
    else:
        num = int(num)
        number.append(num)
        
result = number[0]

for i in range(1,len(number)):
    result-=number[i]

print(result)