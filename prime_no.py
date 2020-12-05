def is_prime(N):
    if N == 2:
        return True
    if N>2:
        for i in range(2, N):
            if N%i == 0:
                return False
        return True
    else:
        return False

N = int(input("Enter the Number: "))
for i in range(1, 101):
    if is_prime(i):
        print(i)
