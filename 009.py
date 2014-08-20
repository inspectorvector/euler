import math

def is_pythag_triplet(a, b, c):
    if a**2 + b**2 == c**2 and a + b + c == 1000:
        return True


def pythagtriplets():

    for a in range(1,1000):
        for b in range(1,1000):
            c = math.sqrt(a**2 + b**2)
            found = is_pythag_triplet(a, b, c)
            if found:
                return a,b,c

print(pythagtriplets())