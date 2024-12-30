import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
targets = list(map(int,input().split()))

results = {}
for card in cards:
    if card in results:
        results[card] += 1
    else:
        results[card] = 1

def binary_search(cards, target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if cards[mid] == target:
        return results.get(target)
    elif cards[mid] < target:
        return binary_search(cards, target, mid+1, end)
    else:
        return binary_search(cards, target, start, mid-1)
    
for target in targets:
    print(binary_search(cards, target, 0, len(cards)-1), end = ' ')