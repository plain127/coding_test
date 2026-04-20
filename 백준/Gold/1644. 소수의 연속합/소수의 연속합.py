import sys

input = sys.stdin.readline

n = int(input())

# 1) 에라토스테네스의 체로 소수 구하기
if n < 2:
    print(0)
    sys.exit()

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

i = 2
while i * i <= n:
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
    i += 1

primes = []
for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)

# 2) 투 포인터
left = 0
current_sum = 0
answer = 0

for right in range(len(primes)):
    current_sum += primes[right]

    while current_sum > n and left <= right:
        current_sum -= primes[left]
        left += 1

    if current_sum == n:
        answer += 1

print(answer)