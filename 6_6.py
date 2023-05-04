# ------------- LESSON 6, EXERCISE 6 -------------------
# Sort the list of random numbers, even firstly than odd

list_of_numbs = [5, 234, 90, 11, 13, 89, 345, 6, 78, 234, 0, 56, 34, 90]


def sort_rand_numbers(lst):
    return list(filter(lambda x: x % 2 == 0, sorted(lst))) + list(filter(lambda x: x % 2 != 0, sorted(lst)))


print(sort_rand_numbers(list_of_numbs))