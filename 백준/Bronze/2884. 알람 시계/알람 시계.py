time = list(map(int,input().split(' ')))
hour=int(time[0])
min=int(time[1])
if (hour >= 0 and hour <= 23):
    if (min >= 0 and min <= 59):
        if(hour>0):
            hour=int((hour * 60 + min - 45) / 60)
            min=int((hour * 60 + min - 45) % 60)
        else:
            if (min < 45):
                hour = 23
                min =60 - abs(min - 45)
            else:
                min = min - 45
        print(hour, min)