T = int(input())
for i in range(T):
    H,W,N = map(int,input().split(" "))
    floor=0
    room=0
    if(1<=H and W<=99 and 1<=N and N<=H*W):
            if(N%H == 0):
                floor = H
                room = N//H
            else:
                floor=N%H
                room=N//H+1
            print(floor*100+room)