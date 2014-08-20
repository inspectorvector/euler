import math

def find_prime(number_of_prime):  # specifies the prime you want to find, eg (10) = 10th prime number
    discovered_primes = []
    current_check = 0
    while len(discovered_primes) < number_of_prime:
        current_check += 1
        if is_prime(current_check):
            discovered_primes.append(current_check)
    return discovered_primes[-1]

def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for n in [2]+list(range(3, math.ceil(math.sqrt(number)) + 1, 2)):
        if number % n == 0:
            return False
    return True


print(find_prime(10001))