import sys

input = sys.stdin.readline

MOD = 10007

comb = [[0]*53 for _ in range(53)]
for i in range(53):
    comb[i][0] = 1
    comb[i][i] = 1

for i in range(2, 53):
    for j in range(1, i):
        comb[i][j] = (comb[i-1][j-1]+comb[i-1][j])%MOD

n = int(input())
ans = 0

for k in range(1,14):
    if 4*k > n:
        break

    four_card_types = comb[13][k]
    rest_cards = comb[52-4*k][n-4*k]
    case_count = (four_card_types*rest_cards)%MOD

    if k%2 == 1:
        ans += case_count
    else:
        ans -= case_count

    ans %= MOD

print(ans)