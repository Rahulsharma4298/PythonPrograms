"""
Find total number of non-empty substrings of a string with N characters.
Here we use the word proper because we do not consider string itself as part of output.

Input : str = "abc"
Output : 6
Proper substrings are "a", "b", "c", "ab", "bc", "abc"

How does above formula work?
==============================

1.Number of substrings of length one is n (We can choose any of the n characters)
2.Number of substrings of length two is n-1 (We can choose any of the n-1 pairs formed by adjacent)
3.Number of substrings of length three is n-2
(We can choose any of the n-2 triplets formed by adjacent)
In general, mumber of substrings of length k is n-k+1 where 1 <= k <= n

Total number of substrings of all lengths from 1 to n =
n + (n-1) + (n-2) + (n-3) + … 2 + 1
= n * (n + 1)/2

"""

def count_non_empty_substring(s):
    n = len(s)
    return int(n * (n + 1)/2)

print(count_non_empty_substring("abc"))
print(count_non_empty_substring("abcd"))
