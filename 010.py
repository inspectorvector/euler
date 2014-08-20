import math

def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for n in [2]+list(range(3, math.ceil(math.sqrt(number)) + 1, 2)):
        if number % n == 0:
            return False
    return True

def primes_up_to_two_mil():

    sum_primes = 2

    for i in range (3, 2000000, 2):
        if is_prime(i):
            sum_primes += i

    return sum_primes

print(primes_up_to_two_mil())
