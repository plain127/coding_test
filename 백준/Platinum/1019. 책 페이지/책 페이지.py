import sys

input = sys.stdin.readline

n = int(input())
ans = [0]*10

def add_num(num, weight):
    while num > 0:
        digit = num%10
        ans[digit] += weight
        num //= 10

start = 1
end = n
weight = 1

while start <= end:
    while start <= end and start%10 != 0:
        add_num(start, weight)
        start += 1

    while start <= end and end%10 != 9:
        add_num(end, weight)
        end -= 1

    if start > end:
        break

    start //= 10
    end //= 10

    block_cnt = end - start + 1

    for digit in range(10):
        ans[digit] += block_cnt*weight
    
    weight *= 10

print(*ans)