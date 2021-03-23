def partion(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]
    
    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    return end


def quick_sort(arr, start, end):
    if start < end:
        pi = partion(arr, start, end)
        quick_sort(arr, start, pi-1)
        quick_sort(arr, pi+1, end)

arr = [3,9,1,7,2,5,10]
print(arr)
quick_sort(arr, 0, len(arr)-1)
print(arr)
