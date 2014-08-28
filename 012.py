def triangle_number_generator(trianglenumwanted):
    tri_num = 0
    for i in range(trianglenumwanted + 1):
        tri_num += i
    return tri_num

def highly_divisible_tri_num():
    list_of_divisors = []
    tri_num = 1

    while len(list_of_divisors) < 501:
        tri_num
