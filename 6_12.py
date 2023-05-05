# ------------- LESSON 6, EXERCISE 12 -------------------
# Write recursive function, received string and reverses it

def reverse_string(line, k=2):
    if k <= len(line):
        line = line[:-k] + line[-k + 1:] + line[-k]
        k += 1
        line = reverse_string(line, k)
    return line

print(reverse_string('abcdefghijklmnopq123'))