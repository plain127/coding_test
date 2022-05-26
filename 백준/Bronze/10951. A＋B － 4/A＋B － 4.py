while True: 
    try:
        A,B = map(int,input().split())
        if(A>0 and B<10):
            print(A+B)
    except EOFError:
        break
        