def reverse_num(N):
    rev = 0
    while(N):
        rev = (rev*10) + N%10
        N = N//10
    return rev

def is_palindrome(N):
    return reverse_num(N) == N

    
N = int(input("Enter the number"))
print(reverse_num(N))
print("Palindrome?", is_palindrome(N))

