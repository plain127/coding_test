n=int(input())
i = 0
while(i<n):
    count = 0
    score = 0
    s = list(input())
    if(len(s)>0 and len(s)<80):
        j = 0
        while(j<len(s)):
            if(s[j]=='O'):
                count+=1
                score+=count
            elif(s[j]=='X'):
                count=0
            j+=1
    print(score)
    i+=1