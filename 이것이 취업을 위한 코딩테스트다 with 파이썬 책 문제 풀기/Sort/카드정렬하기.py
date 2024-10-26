# 내 풀이
n = int(input())
card = []
for _ in range(n):
    card.append(int(input()))

def fibo(card, i):
    if i == 0:
        return card[i]
    
    return card[i] + fibo(card, i - 1)

card.sort()

sum = 0
for i in range(1, len(card)):
    sum += fibo(card, i)
    
print(sum)

# 책 풀이
import heapq

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)
    
result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(heap)