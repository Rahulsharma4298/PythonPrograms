"""
The sieve of Eratosthenes is one of the most efficient ways to find
all primes smaller than n when n is smaller than 10 million or so.

1.Create a list of consecutive integers from 2 to n: (2, 3, 4, …, n).

2.Initially, let p equal 2, the first prime number.

3.Starting from p2, count up in increments of p and mark each of these
numbers greater than or equal to p2 itself in the list. These numbers will be p(p+1), p(p+2), p(p+3), etc..

4.Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise,
let p now equal this number (which is the next prime), and repeat from step 3.

"""
def sieve_of_erastosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2

    while (p*p <= n):
        if(prime[p] == True):
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n+1):
        if prime[p]:
            print(p, end=" ")

n = 11
sieve_of_erastosthenes(n)
 
