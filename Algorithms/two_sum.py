"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may noy use same element twice.

Example:-
    nums = [1,3,11,2,7]
    target = 9
    return [3,4] or print pairs

"""
# Method 1:
"""
# Algorithm:  

->Initialize an empty hash table s.
->Do following for each element A[i] in A[] 
->If s[x – A[i]] is set then print the pair (A[i], x – A[i])
->Insert A[i] into s.

Complexity Analysis:  

Time Complexity: O(n). 
As the whole array is needed to be traversed only once.
Auxiliary Space: O(n). 
A hash map has been used to store array elements.

"""
def print_two_sum_pair(arr, n, target_sum):
    s = set()

    for i in range(n):
        temp =  target_sum - arr[i]
        if temp in s:
            print(arr[i], temp)
        s.add(arr[i])

# Return Indices of pairs
def two_sum(arr, n, target_sum):
    if n <= 1:
        return False
    d = {}
    for i in range(n):
        if arr[i] in d:
            return [d[arr[i]], i]
        else:
            d[target_sum - arr[i]] = i
            

# Method 2:
"""
Brute-Force Approach
O(n^2)

"""
def two_sum_brute_force(arr, n, target_sum):
    for i in range(n - 1):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target_sum:
                print(arr[i], arr[j])
                return True
    return False


# Method 3:
"""
Sorting and Two-Pointers technique.

Complexity Analysis:  

Time Complexity: Depends on what sorting algorithm we use. 
If Merge Sort or Heap Sort is used then (-)(nlogn) in the worst case.
If Quick Sort is used then O(n^2) in the worst case.
Auxiliary Space: This too depends on sorting algorithm.
The auxiliary space is O(n) for merge sort and O(1) for Heap Sort

select max(salary) from Employee e inner join Department d on e.id = d.id group by d.d_id
"""
def two_sum2(arr, n, target_sum):
    i = 0
    j = len(arr)-1

    while i<=j:
        if arr[i] + arr[j] == target_sum:
            print(arr[i], arr[j])
            return True
        elif arr[i] + arr[j] < target_sum:
            i += 1
        else:
            j -= 1
    return False
        

arr = [1,3,11,2,7]
print_two_sum_pair(arr, len(arr), 9)
print(two_sum(arr, len(arr), 9))
two_sum_brute_force(arr, len(arr), 9)
two_sum2(arr, len(arr), 9)
