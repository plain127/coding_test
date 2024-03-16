#내가 푼 풀이
def search(arr, target, start, end, i):
    while (end >=start) :
        mid = (start + end)//2
        if arr[mid] == target[i]:
            print('yes')
        elif arr[mid] > target[i]:
            end = mid -1
        else:
            start = mid +1
    print('no')

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = int(input())
target = list(map(int,input().split()))



for i in range(len(target)):
    search(arr, target, 0, n-1, i)

#책 풀이
    #이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid -1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
        return None

n = int(input())
array = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i , 0, n-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end=' ')

#책 풀이(계수 정렬)
n = int(input())
array = [0] * 1000001

#가게에 있는 전체 부품을 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

# M(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end =' ')


#책풀이 (집합 자료형 이용)
n = int(input())
#가게에 있는 전체 부품을 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
        