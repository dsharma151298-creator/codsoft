import random
import string

size = int(input("Password length: "))

chars_letters = string.ascii_letters
chars_numbers = string.digits
chars_symbols = string.punctuation

pwd_list = [
    random.choice(chars_letters),
    random.choice(chars_numbers),
    random.choice(chars_symbols)
]

for _ in range(size - 3):
    pwd_list.append(random.choice(chars_letters + chars_numbers + chars_symbols))

random.shuffle(pwd_list)

final_password = "".join(pwd_list)

print("Your password is:", final_password)