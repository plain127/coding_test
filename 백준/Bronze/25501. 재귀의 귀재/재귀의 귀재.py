def recursion(s,l,r, count):
    if l >= r:
        return 1, count
    elif s[l] != s[r]:
        return 0, count
    else:
        count += 1
        return recursion(s, l+1, r-1, count)

def isPalindrome(s,count):
    return recursion(s, 0, len(s)-1, count)

t = int(input())

results = []

for _ in range(t):
    s = input()
    count = 1
    results.append(isPalindrome(s, count))

for result in results:
    print(result[0], result[1])