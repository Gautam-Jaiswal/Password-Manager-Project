import random

def encryption(s):
    encrypted_string = ''
    encode_by = random.randint(26, 50)

    for char in s:
        x = ord(char)+encode_by
        if x > 126:
            x = x - 126 + 33
        encrypted_string += chr(x)
    encrypted_string += str(encode_by)

    return encrypted_string

def decryption(s):
    decrypted_string = ''
    decode_value = int(s[-2:])

    for char in s[:-2]:
        x = ord(char) - decode_value
        if x < 33:
            x = x + 126 - 33
        decrypted_string += chr(x)

    return decrypted_string

def create_new_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letter_count = random.randint(7,12)
    numbers_count = random.randint(3, 7)
    symbols_count = random.randint(2, 6)

    password = []

    for char in range(letter_count):
        password.append(random.choice(letters))

    for char in range(symbols_count):
        password += random.choice(symbols)

    for char in range(numbers_count):
        password += random.choice(numbers)

    random.shuffle(password)

    password = ''.join(password)

    return password
