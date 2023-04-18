# ------------- LESSON 3, EXERCISE 1 -------------------
# User enter the statement, replace all gaps with '-' symbols by 2 different ways

input_text = input('enter any text>')

# 1st way:
print(input_text.replace(' ', '-'))

# 2nd way:
split_text = input_text.split(' ')
print('-'.join(split_text))

