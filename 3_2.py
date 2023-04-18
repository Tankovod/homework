# ------------- LESSON 3, EXERCISE 2 -------------------
# User enters 3 numbers, find average with precision 3

# -------- 1st way ---------
first_number = int(input('enter the first number>'))
second_number = int(input('enter the second number>'))
third_number = int(input('enter the third number>'))

summa = first_number + second_number + third_number
print(round(summa / 3, 3))
# -------- 1st way ---------

# -------- 2nd way ---------
numbers = []
summ = 0

try:
    input_numbers = input('enter any numbers through gaps>')
    numbers_list = input_numbers.strip().split(' ')

    for number in numbers_list:
        numbers.append(int(number))
        summ += int(number)

    print(round(summ / len(numbers), 3))
    print(round(sum(numbers) / len(numbers), 3))

except Exception as ex_:
    print(ex_)
    print('!__check your input data__!')
# -------- 2nd way ---------
