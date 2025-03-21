import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())
m = 2**n
count = 0

def dc(row, col, num):
    global count
   
    if row > r or row + num <= r or col > c or col + num <= c:
        count += num**2
        return
   
    if num > 2:
        num//=2
        dc(row, col, num)
        dc(row, col+num, num)
        dc(row+num, col, num)
        dc(row+num, col+num, num)
    else:
        if row == r and col == c:
            print(count)
        elif row == r and col+1 == c:
            print(count+1)
        elif row+1 == r and col == c:
            print(count+2)
        else:
            print(count+3)
        sys.exit()

dc(0,0,m)
