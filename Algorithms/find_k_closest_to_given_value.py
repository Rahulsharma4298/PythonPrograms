"""
Given a sorted array arr[] and a value X, find the k closest elements to X in arr[].
Examples:

Input: K = 4, X = 35
       arr[] = {12, 16, 22, 30, 35, 39, 42, 
               45, 48, 50, 53, 55, 56}
Output: 30 39 42 45

Note that if the element is present in array,
then it should not be in output, only the other closest elements are required.

A simple solution is to do linear search for k closest elements.
1) Start from the first element and search for the crossover point (The point before which elements are smaller than or equal to X and after which elements are greater).
This step takes O(n) time.
2) Once we find the crossover point, we can compare elements on both sides of crossover point to print k closest elements.
This step takes O(k) time.

The time complexity of the above solution is O(n).


An Optimized Solution is to find k elements in O(Logn + k) time.
The idea is to use Binary Search to find the crossover point.
Once we find index of crossover point, we can print k closest elements in O(k) time.

"""

def binary_search(arr, x):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return low

def find_k_closest(arr, x, k):
    i = binary_search(arr, x)
    left = i - 1
    right = i

    while k > 0:
        if left < 0 or (right < len(arr) and abs(arr[left]-x) > abs(arr[right]-x)):
            right = right + 1
        else:
            left = left - 1
        k = k - 1

    print(arr[left+1:right])

"""
The above solution to do a binary search to find the insertion point and then tries to find the
closest elements. However, we can combine the whole logic in a single binary search routine.

"""

def findKClosest(arr, x, k):
    left = 0
    right = len(arr)-1
    while(right - left >= k):
        if abs(arr[left] - x) > abs(arr[right] - x):
            left = left + 1
        else:
            right = right - 1

    print(arr[left:left+k])
            
arr = [10, 12, 15, 17, 18, 20, 25]
x = 16
k = 3
find_k_closest(arr, x, k)
findKClosest(arr, x, k)
            
                        
        
                        
        
        
        
    
    
    
