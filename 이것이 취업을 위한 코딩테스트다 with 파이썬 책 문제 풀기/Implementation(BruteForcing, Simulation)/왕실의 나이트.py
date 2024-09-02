#내가 푼 풀이
loc = input()

count = 0

if ord(loc[0]) < ord('g') and ord(loc[0]) > ord('b'):
    if int(loc[1]) > 1 and int(loc[1]) < 8:
        count += 8
    else:
        count += 4
else:
    if int(loc[1]) > 1 and int(loc[1]) < 8:
        count += 4
    else:
        count += 2

print(count)

#책 풀이
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
        
print(result)