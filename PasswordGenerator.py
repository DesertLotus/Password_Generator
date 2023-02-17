import random

def good_password_generator(length):
    letters = 'abcdefgihjklmnopqrstuvwxyz'
    upper_letters = 'ABCDEFGIHJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = '!@#$%^&*()_+-=\'\\"'

    alphabet = letters + upper_letters + digits + symbols

    password = ''
    for i in range(length):
        char = random.choice(alphabet)
        password += char

    return password


length = int(input("Enter a length of the password you want: "))
password = good_password_generator(length)
print(password)