def triangle_number_generator(trianglenumwanted):
    tri_num = 0
    for i in range(trianglenumwanted + 1):
        tri_num += i
    return tri_num

def highly_divisible_tri_num():
    list_of_divisors = []
    current_tri_num = 1

    while len(list_of_divisors) < 501:
        for i in range(1, triangle_number_generator(current_tri_num) + 1):
            if current_tri_num % i == 0:
                list_of_divisors.insert(i, i)
        current_tri_num += 1
    print(list_of_divisors)
    return current_tri_num

print(highly_divisible_tri_num())