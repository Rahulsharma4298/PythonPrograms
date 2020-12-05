def is_armstrong(N):
    temp = N
    r = 0
    while temp:
        digit = temp%10
        r = r+(digit**3)
        temp = temp//10

    if N == r:
        return True
    return False
    
#N = int(input())
#print(is_armstrong(N))

lower = 100
upper = 2000

for i in range(lower, upper+1):
    if is_armstrong(i):
        print(i)
        
    
        
