def is_palindrome(number):
    number = str(number)
    number2 = number
    n = 0
    for i in number2[::-1]:
        if i != number[n]:
                return False
        n += 1
    return True


def multiplication():
    n1 = 999
    n2 = 999
    largest_palindrome = 0
    while n1 > 99:
        current_answer = n1 * n2
        print(n1, n2, current_answer)
        if is_palindrome(current_answer):
            if current_answer > largest_palindrome:
                largest_palindrome = current_answer
        n2 -= 1
        if n2 == 99:
            n2 = 999
            n1 -=1
    return largest_palindrome

print(multiplication())
