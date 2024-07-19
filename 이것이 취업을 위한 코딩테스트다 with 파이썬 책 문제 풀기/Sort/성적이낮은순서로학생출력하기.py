# 내가 푼 풀이
n = int(input())

name_score = {}

for i in range(n):
    name, score = input().split()
    name_score[name] = int(score)
    
score = sorted(name_score)

print(score, end=' ')

# 책 풀이

n = int(input())

array = []

for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
    
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')