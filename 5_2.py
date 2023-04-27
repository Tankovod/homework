# ------------- LESSON 5, EXERCISE 2 -------------------
# Make the calculator, where user will be asked for first number,
# then for action and then for second number

first_number = int(input('The first number>'))
action = input('The action>').strip()
second_number = int(input('The second number>'))

if action == '/':
    print(first_number / second_number)
elif action == '+':
    print(first_number + second_number)
elif action == '-':
    print(first_number - second_number)
elif action == '*':
    print(first_number * second_number)
elif action == '%':
    print(first_number % second_number)
elif action == '**':
    print(first_number ** second_number)
else:
    print('--- Error. Check your input data ---')





