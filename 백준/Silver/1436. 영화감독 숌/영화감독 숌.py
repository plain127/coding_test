n = int(input())

movie = []

i = 665
while True:
    i+=1
    if '666' in str(i):
        movie.append(i)
    if len(movie) == n:
        break
movie.sort(reverse=True)

print(movie[0])