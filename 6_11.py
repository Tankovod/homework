# ------------- LESSON 6, EXERCISE 11 -------------------
# Write function generator, received int count and return count amount simple numbers
from math import sqrt

def generate_simple_nums(count):
    number = 1
    for elem in range(1, count + 1):
        if number != 1:
            while any([number for i in range(2, number // 2 + 1) if number % i == 0]) and number not in [2, 3, 5, 7]:
                number += 1
            yield number
        number += 1


print([*generate_simple_nums(100)])
