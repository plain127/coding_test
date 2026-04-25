import sys

input = sys.stdin.readline

def solve(heights):
    n = len(heights)
    stack = []
    ans = 0

    for idx in range(n+1):
        if idx == n:
            height = 0
        else:
            height = heights[idx]

        start = idx

        while stack and stack[-1][-1] > height:
            old_start, old_height = stack.pop()

            area = old_height*(idx-old_start)

            if ans < area:
                ans = area

            start = old_start
        
        stack.append((start, height))
    return ans

ans = []

while True:
    data = list(map(int, input().split()))

    if data[0] == 0:
        break

    n = data[0]
    heights = data[1:]

    ans.append(str(solve(heights)))

print('\n'.join(ans))
