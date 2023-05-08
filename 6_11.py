# ------------- LESSON 6, EXERCISE 11 -------------------
# Write function generator, received int count and return count amount simple numbers


def generate_simple_nums(count):
    number = 2
    for elem in range(1, count + 1):
        if number not in [2, 3, 5, 7]:
            tim = 0
            while tim == 0:
                tim = 1
                for divider in range(2, number // 2 + 1):
                    if number % divider == 0:
                        number += 1
                        tim = 0
                        break
        yield number
        number += 1


print([*generate_simple_nums(100)])
