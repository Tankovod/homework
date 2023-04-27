# ------------- LESSON 5, EXERCISE 1 -------------------
# Show the first N entire numbers, multiple of M and more than K

N = int(input('Show the amount of entire numbers>'))
M = int(input('A multiple of>'))
K = int(input('And more than>'))

amount_of_numbers = 0
list_of_numbers = []
sort_out = 0

while amount_of_numbers < N:
    if sort_out % M == 0 and sort_out > K:
        list_of_numbers.append(sort_out)
        amount_of_numbers += 1
    sort_out += 1

print(list_of_numbers)

