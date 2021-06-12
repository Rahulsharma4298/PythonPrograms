# Find No. of Trailing zeros in factorial of a number n.
# Example: 
# Input: n = 5
# Output: 1 
# Approach:
# A simple method is to first calculate factorial of n, then count trailing 0s in the result 
# (We can count trailing 0s by repeatedly dividing the factorial by 10 till the remainder is 0).
 
# The above method can cause overflow for slightly bigger numbers as the factorial of a number is a big number.
 
# We can easily observe that the number of 2s in prime factors is always more than or equal to the number of 5s.
# So if we count 5s in prime factors, we are done.

# -A simple way is to calculate floor(n/5).
# -For example, 7! has one 5, 10! has two 5s. It is not done yet, there is one more thing to consider.
# -Numbers like 25, 125, etc have more than one 5. For example, if we consider 28! we get one extra 5 and the number of 0s becomes 6.
# -Handling this is simple, first, divide n by 5 and remove all single 5s, then divide by 25 to remove extra 5s, and so on.

# Trailing 0s in n! = Count of 5s in prime factors of n!
#                   = floor(n/5) + floor(n/25) + floor(n/125) + ....


n = 10
i = 5
count = 0
while n//i > 0:
	count += n//i
	i *= 5

print(count)
