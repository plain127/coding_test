#내가 푼 풀이
loc = input()

loc_x = int(ord(loc[0])) - 96
loc_y = loc[1]

dx = [-2,-1,1,2]
dy = [-2,-1,1,2]

count = 0
#gg

#책 풀이
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8:
        result +=1
print(result)