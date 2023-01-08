# Exercise 11 -  Check Primality Functions

# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.


prime = int(input("Provide a number to find if it's a prime number: \n"))
a = [x for x in range(2, prime) if prime % x == 0]
b = []


def get_prime(n):
    if prime > 1:
        if len(a) == 0:
            print('prime')
        else:
            print('NOT prime')
    else:
        print('NOT prime')


get_prime(prime)