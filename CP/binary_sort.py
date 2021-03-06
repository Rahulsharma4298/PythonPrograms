"""
Sort the array on basis of number of ones in binary form of array elements
in decresing order.

"""


def binary_sort(arr):
    b = []
    arr.sort(reverse=1)
    for i in arr:
        binary = bin(i)[2:]
        print(i, binary)
        b.append(binary)

    a = sorted(b, reverse=1, key=lambda x: x.count('1'))
    x = sorted(b, reverse=1)
    print(list(x))
    result = []
    for i in a:
        int_of_bin = int(i, 2)
        result.append(int_of_bin)
    print(result)
       

arr = [5,3,7,4,5]
binary_sort(arr)
    
        
    
    
