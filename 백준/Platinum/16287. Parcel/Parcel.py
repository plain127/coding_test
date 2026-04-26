import sys

input = sys.stdin.readline

def main():
    w, n = map(int, input().split())
    weights = list(map(int, input().split()))

    can_pair = [False]*(w+1)

    for i in range(n):
        for j in range(i+1, n):
            current_sum = weights[i] + weights[j]

            target = w - current_sum

            if 0<=target<=w and can_pair[target]:
                print('YES')
                return
        
        for j in range(i):
            pair_sum = weights[i] + weights[j]

            if pair_sum <= w:
                can_pair[pair_sum] = True

    print('NO')

main()