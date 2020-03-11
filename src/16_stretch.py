"""
 Write a program to determine if a number, given on the command line, is prime.

   1. How can you optimize this program?
   2. Implement [The Sieve of
      Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
      of the oldest algorithms known (ca. 200 BC).

    Requirements for prime
    - greater than 1
    - any even number that is greater than 2 is not prime
    
    1.Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
    2.Initially, let p equal 2, the smallest prime number.
    3.Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
    4.Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
    5.When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.
"""
# Will revise later


def isItPrime(num):
    nums = [x for x in range(2, num + 1)]
    # cross out every 2nd number in the list after 2 by counting up from 2 in increments of
    numbers = [2, 3, 5, 7]
    for x in nums:
        if x in numbers:
            comp = nums[x:]
            for y in comp:
                if y % x == 0:
                    nums.remove(y)

    if num in nums:
        return str(num) + " is a prime number"
    else:
        return str(num) + " is not a composite number"


print(isItPrime(2))
print(isItPrime(3))
print(isItPrime(4))
print(isItPrime(7))
print(isItPrime(5))
print(isItPrime(67))
print(isItPrime(32))
print(isItPrime(55))
print(isItPrime(77))
