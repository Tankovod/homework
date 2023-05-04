# ------------- LESSON 6, EXERCISE 3 -------------------
# displace list for N symbols

def displace_list(n):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 123, 324, 243, 34, 5, 354, 356, 34]
    if n < len(num_list):
        return num_list[-n:-1] + num_list[:-n]
    else:
        return 'Too big number to displace'

print(displace_list(int(input('Number of symbols in list to displace>'))))