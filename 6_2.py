# ------------- LESSON 6, EXERCISE 2 -------------------
# Write the function to encode string into Morse code

def to_encode_morse(strng):
    morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..--', '3': '...--', '4': '....-',
                  '5': '.....', '6': '-....', '7': '--..', '8': '---..', '9': '----.'}

    for symbol in strng:
        if symbol.upper() not in morse_dict.keys():
            return '!!! Enter valid string !!!'

    return ' '.join([morse_dict.get(i) for i in strng.upper().replace(' ', '')])


while ...:
    print(to_encode_morse(input('Enter any words or integers to morse>')))
