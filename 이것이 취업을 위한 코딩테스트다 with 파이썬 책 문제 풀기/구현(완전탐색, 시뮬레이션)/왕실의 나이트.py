#나의 풀이

#책 풀이
pos = input()
row = int(pos[1])
col = int(ord(pos[0])) - int(ord('a')) + 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
count = 0

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    if next_row >=1 and next_row <= 8 and next_col >=1 and next_col <=8:
        count += 1
        
print(count)