# ------------- LESSON 3, EXERCISE 3 -------------------
# User enters name, age, city; form welcome message by formatting by 3 ways

name = input('enter your name>')
age = int(input('enter your age>'))
city = input('enter your city>')

# 1st way:
print(f'Hello, {name}! You are {age} years old and you are from {city}.')
# 2nd way:
print('Hello, %s! You are %d years old and yoe are from %s.' % (name, age, city))
# 3rd way:
print('Hello, {user_name}! You are {user_age} years old and you are from {user_city}.'.format(user_name=name,
                                                                                              user_age=age,
                                                                                              user_city=city))
