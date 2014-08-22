import math

def largest_prime_factor(number):
    largest_prime = number
    n = 2
    while n < largest_prime:
        if largest_prime % n == 0:
            largest_prime = largest_prime/n
        else:
            n = next_prime(n)
    return largest_prime

def next_prime(number):
    next = number+1
    while not is_prime(next):
        next += 1
    return next


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for n in [2]+list(range(3, math.ceil(math.sqrt(number)) + 1, 2)):
        if number % n == 0:
            return False
    return True


print(largest_prime_factor(600851475143))