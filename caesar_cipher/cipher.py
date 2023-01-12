from caesar_cipher.is_english_text import is_english


def encrypt(text, n):
    encrypted = ''
    for char in text:
        # returns true if char is an english alphabet letter
        if char.isalpha():
            # ord function returns an int representing the unicode character
            char_code = ord(char)
            # since upper and lower case have different codes we have to have 2 conditions
            if char.islower():
                shift_chr_code = (char_code - 97 + n) % 26 + 97 # lower case starts at unicode 97
            elif char.isupper():
                shift_chr_code = (char_code - 65 + n) % 26 + 65  # upper case starts at unicode 65
            encrypted += chr(shift_chr_code)  # chr converts back to a string char
        else:
            encrypted += char
    return encrypted


def decrypt(text, n):
    decrypted = ''
    for char in text:
        # returns true if char is an english alphabet letter
        if char.isalpha():
            # ord function returns an int representing the unicode character
            char_code = ord(char)
            # since upper and lower case have different codes we have to have 2 conditions
            if char.islower():
                shift_chr_code = (char_code - 97 - n) % 26 + 97  # lower case starts at unicode 97
            elif char.isupper():
                shift_chr_code = (char_code - 65 - n) % 26 + 65  # upper case starts at unicode 65
            decrypted += chr(shift_chr_code)  # chr converts back to a string char
        else:
            decrypted += char
    return decrypted


def crack(text):
    for i in range(26):
        if is_english(decrypt(text, i)):
            return decrypt(text, i)
    return ''
