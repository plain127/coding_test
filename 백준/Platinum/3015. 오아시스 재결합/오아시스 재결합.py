import sys

input = sys.stdin.readline

n = int(input())
stack = []
answer = 0

for _ in range(n):
    height = int(input())
    cnt = 1

    while stack and stack[-1][0] < height:
        small_height, small_cnt = stack.pop()
        answer += small_cnt

    if stack and stack[-1][0] == height:
        same_height, same_cnt = stack.pop()
        answer += same_cnt
        cnt = same_cnt + 1

        if stack:
            answer += 1
    else:
        if stack:
            answer += 1
    stack.append((height, cnt))

print(answer)