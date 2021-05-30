def reverse_array(a, n):
    b = [0]*n
    j = n
    for i in range(n):
        b[j-1] = a[i]
        j = j - 1
    print("Reversed array is:")
    print(b)
    
def reverse_array2(a, n):
    for i in range(n//2):
        temp = a[i]
        a[i] = a[n-i-1]
        a[n-i-1] = temp
    print("Reversed array is:")
    print(a)
    
    
a = [2,4,6,8,0]
reverse_array(a, len(a))
reverse_array2(a, len(a))

