import math

def is_pronic(N):
    x = (int)(math.sqrt(N))
    if x*(x+1) == N:
        return 1
    else:
        return 0

N = int(input("Enter the number: "))
if is_pronic(N):
    print("YES")
else:
    print("NO")

for i in range(1,101):
    if is_pronic(i):
        print(i)
