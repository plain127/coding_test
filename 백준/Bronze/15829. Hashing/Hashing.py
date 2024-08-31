l = int(input())
alphas = input()

result = 0

for idx, alpha in enumerate(alphas):
    result += (ord(alpha) - 96)*(31**idx)
    
print(result%1234567891)