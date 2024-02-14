#내가 푼 풀이
n = int(input())

dic = {}

for i in range(n):
    name, score = input().split()
    dic[score] = name

score_list = []

for i in dic.keys():
    
    score_list.append(i)

score_list.sort()

for i in score_list:
    print(dic[i], end=" ")

#책 풀이
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append(input_data[0], int(input_data[1]))

array = sorted(array, key=lambda student:student[1])

for student in array:
    print(student[0], end = ' ')
    