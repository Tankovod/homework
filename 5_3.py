# ------------- LESSON 5, EXERCISE 3 -------------------
# Display even numbers from 2 to N 5 per line

# ----- 1st way -----
N = int(input('Enter maximum number>'))

list_of_numbers = [number for number in range(2, N) if number % 2 == 0]

list_index = 0
while list_index < len(list_of_numbers):
    print(str(list_of_numbers[list_index:list_index + 5])[1:-1])
    list_index += 5
# ----- 1st way -----

print('---------------------')

# ----- 2nd way -----
list_index = 0
string_of_num5 = ''
for number in list_of_numbers:
    if list_index < 5:
        string_of_num5 += ' ' + str(number)
        list_index += 1
    else:
        print(string_of_num5)
        string_of_num5 = str(number)
        list_index = 1
        continue
print(string_of_num5)
# ----- 2nd way -----

