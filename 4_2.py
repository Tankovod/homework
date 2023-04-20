# ------------- LESSON 4, EXERCISE 2 -------------------
# Without using collections, write the program, that will create a dictionary to
# count the number of entries of each letter in the text entered from the keyboard.

input_text = input('Enter any text>')
list_of_letters = list(input_text)

print('Input line: ' + str(list(input_text)))

count_of_letters_dict = {}

for letter in list_of_letters:
    count = 0
    while letter not in count_of_letters_dict:  # to improve comparing
        for other_letter in list_of_letters:
            if letter == other_letter:
                count += 1
                count_of_letters_dict[f'{letter}'] = count
            else:
                pass

print('Count of letters: ' + str(count_of_letters_dict))
