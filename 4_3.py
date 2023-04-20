# ------------- LESSON 4, EXERCISE 3 -------------------
# Fill in the dictionary where keys are from 0 to n, values are the
# nested dictionary with keys 'name' and 'email' and meanings for these
# keys will be taken from the keyboard

users_dict = {1: {'name': 'Jack', 'email': 'tool@gmail.com'}, 4: {'name': 'Daniel', 'email': 'zebra@email.com'}}

circle = True
while circle:
    user_name = input('Enter the user\'s name>')
    user_email = input('Enter the user\'s email>')

    max_id = max(users_dict.keys())
    users_dict[max_id + 1] = {'name': user_name, 'email': user_email}

    print(users_dict)
