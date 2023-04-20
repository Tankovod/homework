# ------------- LESSON 4, EXERCISE 1 -------------------
# Fill in list with degrees of number 2 (from 2^1 to 2^n)

max_range = int(input('The number of elements in 2^n list>'))

degrees_list = [2 ** n for n in range(1, max_range + 1)]  # list comprehension
print(degrees_list)
