# ------------- LESSON 6, EXERCISE 5 -------------------
# Reverse list of integers without using of reverse(), slice and additional list

list_to_reverse = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 33, 44, 100, 101, 10001, 345345, 0, 0, 4, 5, 6, 8, 9]

def reverse_the_list(lst):
    last = len(lst)
    for i in range(len(lst), 0, -1):
        lst.append(lst[i - 1])
    for i in range(last):
        lst.pop(0)
    return lst


print(reverse_the_list(list_to_reverse))