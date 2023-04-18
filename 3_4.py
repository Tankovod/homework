# ------------- LESSON 3, EXERCISE 3 -------------------
# User enters 3 numbers, display the counts of positive and negative values

positive = 0
negative = 0
numbers_list = []

# ----- 1st way ---------
numbers_list.append(input('enter the first number>').strip())
numbers_list.append(input('enter the second number>').strip())
numbers_list.append(input('enter the third number>').strip())

for number in numbers_list:
    if number.startswith('-') and number[1:].isdigit():
        negative += 1
    elif number.isdigit():
        positive += 1
    else:
        print('!__check your input data__!')

print(f'There are {positive} positive and {negative} negative values.')
# ----- 1st way ---------

# ------- 2nd way -------
# try:
#     numbers_list.append(int(input('enter the first number>')))
#     numbers_list.append(int(input('enter the second number>')))
#     numbers_list.append(int(input('enter the third number>')))
#
#     for number in numbers_list:
#         if number < 0:
#             negative += 1
#         else:
#             positive += 1
#
#     print(f'There are {positive} positive and {negative} negative values.')
#
# except Exception as ex_:
#     print(ex_)
#     print('!__check your input data__!')
# ------- 2nd way -------

