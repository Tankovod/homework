# ------------- LESSON 5, EXERCISE 6 -------------------
# <<<Guess the number>>>
# You need to write the game "Guess the number" and
# show how many times user attempt to guess it

from random import randint

a = randint(1, 100)
# print(a)

attempts, guess = 0, None
while guess != a:
    try:
        guess = int(input('Guess the number !!:D >'))
        attempts += 1
    except ValueError:
        print('Try any whole number, please ...')

print(f'Congratulations !!! You had to guess {attempts} times ! XD')
