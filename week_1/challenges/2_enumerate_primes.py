'''
A prime number (or a prime) is an integer greater than 1 that has no positive divisors other than 1 and itself.

Write a program which takes as input an int value n and returns an array of int containing all unique primes <= n.

Example: if the value of n is 8, the function should return: {2,3,5,7}

Hint: One well-known algorithm for doing this is over 2,000 years old, but it's not the most efficient.

Remember, you are not allowed to use any primality testing functions.
'''
import math

def enumeratePrimes(n):

    # Instantiate all numbers as initially True
    primes = [True] * (n+1)
    # Instantiate 0 and 1 to False
    primes[0], primes[1] = [False]*2

    result = []

    sqrt = int(math.ceil(math.sqrt(n)))

    # Iterate from 2 ->
    for i, prime in enumerate(primes[2:sqrt], 2):
        # If the current number is True (prime)
        if primes[i]:

            # j = 1
            # while i*j <= n:
            #     primes[i*j] = False
            #     j+=1

            # Mark all multiples of this value as False
            primes[i*i::i] = [False for val in primes[i*i::i]]

    # Find all prime numbers
    for i, prime in enumerate(primes):
        if prime:
            result.append(i)

    return result

print enumeratePrimes(8)
