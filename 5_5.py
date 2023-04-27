# ------------- LESSON 5, EXERCISE 5 -------------------
# Calculate average of the N numbers entered from the keyboard

list_of_numbers = [int(number) for number in input('Enter numbers through spaces>').strip().split(' ')]

# ----- 1st way -----
summ = 0
for number in list_of_numbers:
    summ += number
print(f'Average of the numbers is: {summ / len(list_of_numbers)}')
# ----- 1st way -----

# ----- 2nd way -----
print(f'Average of the numbers is: {sum(list_of_numbers) / len(list_of_numbers)}')
# ----- 2nd way -----
