import sys

input = sys.stdin.readline

a, b = map(int, input().split())

def cnt_one(x):
    if x < 0:
        return 0

    bit = 1
    total = 0

    while bit <= x:
        cycle = 2*bit
        total += (x+1)//cycle*bit
        remainder = (x+1)%cycle
        total += max(0, remainder-bit)

        bit*=2

    return total

print(cnt_one(b)-cnt_one(a-1))