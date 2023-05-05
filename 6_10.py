# ------------- LESSON 6, EXERCISE 10 -------------------
# Write generator received 3 arguments (number, start, end), all arguments
# are integers. Generator must return number in degree from start to end

def generate_degree(number, start, end):
    for degree in range(start, end + 1):
        yield number ** degree


ref = generate_degree(21, 2, 7)
# print(list(ref))
print(next(ref))
print(next(ref))
print(next(ref))
