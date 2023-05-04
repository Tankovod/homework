# ------------- LESSON 6, EXERCISE 1 -------------------
# Write the function to transfer decimal number into the
# binary and back, without using of function int

def change_bit_depth(number):
    bin_num = bin(number).replace('0b', '')
    return sum([2 ** i for i in range(len(bin_num)) if bin_num[::-1][i] == '1'])


result = change_bit_depth(7788)
print(result)
