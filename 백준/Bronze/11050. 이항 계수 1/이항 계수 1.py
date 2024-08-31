n, k = map(int,input().split())

def facto(n):
    if n > 1:
        return n * facto(n-1)
    else:
        return 1
    
result = facto(n) // (facto(k)*facto(n-k))
print(result)