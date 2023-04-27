# ------------- LESSON 5, EXERCISE 4 -------------------
# Find maximum digit of entered number

input_number = input('Enter any entire number>')

list_of_digits = [int(digit) for digit in input_number.strip()]

# ----- 1st way -----
print('Maximum digit is ' + str(max(list_of_digits)))
# ----- 1st way -----

# ----- 2nd way -----
print('Maximum digit is ' + str(max_digit := sorted(list_of_digits)[::-1][0]))
# ----- 2nd way -----

# ----- 3rd way -----
for i in range(0, len(list_of_digits)):
    minimum = i

    for j in range(i + 1, len(list_of_digits)):
        if list_of_digits[j] < list_of_digits[minimum]:
            minimum = j

    list_of_digits[minimum], list_of_digits[i] = list_of_digits[i], list_of_digits[minimum]

print('Maximum digit is ' + str(list_of_digits[-1]))
# ----- 3rd way -----

