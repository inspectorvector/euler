def division(number):
    i = 20
    while i > 0:
        if number % i != 0:
            break
        elif i == 1:
            return number
        i -= 1


def smallest_multiple():
    number_to_check = 1
    while division(number_to_check) is None:
        number_to_check += 1
    print(number_to_check)


smallest_multiple()