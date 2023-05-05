# ------------- LESSON 6, EXERCISE 7 -------------------
# Count sum of it's neighbors for number in list of numbers
# If elements are last or first, it's first and last values accordingly

list_of_numbers = [1, 34, 5, 34, 567, 56, 89, 0, 235, 78, 23, 5, 7, 14236, 5467, 4]


def sum_neighbours(lst):
    return [(lst[i], f'Sum is {sum([lst[i - 1], lst[i + 1]])}') if i < len(lst) - 1
            else (lst[i], f'Sum is {lst[i - 1] + lst[0]}') for i in range(len(lst))]


print(sum_neighbours(list_of_numbers))
