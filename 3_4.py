# ------------- LESSON 3, EXERCISE 4 -------------------
# User enters 3 numbers, display the counts of positive and negative values

# ----- 1st way ---------

first_number = input('enter the first number>')
second_number = input('enter the second number>')
third_number = input('enter the third number>')

num3_list = first_number + second_number + third_number

negative = num3_list.count('-')
positive = 3 - negative

print(f'There are {positive} positive and {negative} negative values.')
# ----- 1st way ---------

# ------- 2nd way -------
positive, negative = 0, 0

numbers_list = [input('enter the first number>').strip(),
                input('enter the second number>').strip(),
                input('enter the third number>').strip()]

err = 0
for number in numbers_list:
    if number.startswith('-') and number[1:].isdigit():
        negative += 1
    elif number.isdigit():
        positive += 1
    else:
        print(f'!__The value \'{number}\' was not processed. Check your input data__!')
        err = 1

if err == 0:
    print(f'There are {positive} positive and {negative} negative values.')
else:
    pass
# ------- 2nd way -------

# ------- 3rd way -------
positive, negative = 0, 0
try:

    numbers_list = [int(input('enter the first number>')),
                    int(input('enter the second number>')),
                    int(input('enter the third number>'))]

    for number in numbers_list:
        if number < 0:
            negative += 1
        else:
            positive += 1

    print(f'There are {positive} positive and {negative} negative values.')

except Exception as ex_:
    print(ex_)
    print('!__check your input data__!')
# ------- 3rd way -------
