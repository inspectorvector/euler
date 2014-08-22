def fibonacci():
    a = 1
    b = 2
    total = 2
    n = 0
    while n < 4000000:
        n = a + b
        if n % 2 == 0:
            total += n
        a = b
        b = n
    return total

print(fibonacci())


