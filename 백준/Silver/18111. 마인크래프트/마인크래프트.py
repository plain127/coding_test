import sys 
input = sys.stdin.readline

def get_time(h):
    add_num = 0   
    erase_num = 0  

    
    for i in range(257): 
        n, tmp = nums[i], i - h 
         
        if n == 0: 
            continue 
         
        if tmp < 0:
            add_num += (-tmp) * n 
         
        else:
            erase_num += tmp * n 
    
     
    if (erase_num + b) - add_num >= 0:
         
        time = erase_num * 2 + add_num 
        return time 
    
    else:
        return 1e9 + 1
            
n, m, b = map(int,input().split())


nums = [0] * 257 
for i in range(n):
    for j in list(map(int,input().split())):
        nums[j] += 1 


ans = 1e9 
height = 0


for h in range(257):

    time = get_time(h)

    if time <= ans:
        ans = time 
        height = h 

print(ans, height)