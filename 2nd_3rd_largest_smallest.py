def second_largest(arr):
    first_max = second_max = -2147483648
    for i in range(len(arr)):
        if arr[i] > first_max:
            second_max = first_max
            first_max = arr[i]
        elif arr[i] > second_max and arr[i] != first_max:
            second_max = arr[i]
            
    if (second_max == -2147483648):
        print("The first largest element is", first_max)
        print("There is no second largest element")
    else:
        print("The first largest element is", first_max)
        print("The second largest element is", second_max)

def second_smallest(arr):
    first_min = second_min = 2147483648
    for i in range(len(arr)):
        if arr[i] < first_min:
            second_min = first_min
            first_min = arr[i]
        elif arr[i] < second_min and arr[i] != first_min:
            second_min = arr[i]
            
    if (second_min == 2147483648):
        print("The first smallest element is", first_min)
        print("There is no second smallest element")
    else:
        print("The first smallest element is", first_min)
        print("The second smallest element is", second_min)

def third_largest(arr):
    first_max = second_max = third_max = -2147483648
    for i in range(len(arr)):
        if arr[i] > first_max:
            third_max = second_max
            second_max = first_max
            first_max = arr[i]
        elif arr[i] > second_max and arr[i] != first_max:
            third_max = second_max
            second_max = arr[i]
        elif arr[i] > third_max and arr[i] != second_max:
            third_max = arr[i]
    print(first_max, second_max, third_max)

def third_smallest(arr):
    first_min = second_min = third_min = 2147483648
    for i in range(len(arr)):
        if arr[i] < first_min:
            third_min = second_min
            second_min = first_min
            first_min = arr[i]
        elif arr[i] < second_min and arr[i] != first_min:
            third_min = second_min
            second_min = arr[i]
        elif arr[i] < third_min and arr[i] != second_min:
            third_min = arr[i]

    print(first_min, second_min, third_min)
   


arr = [5,4,8,3,6,1,2]
second_largest(arr)
second_smallest(arr)
third_largest(arr)
third_smallest(arr)

    
    
