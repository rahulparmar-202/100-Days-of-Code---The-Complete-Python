import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Version
# password = ""
#
# for char in range(0,nr_letters):
#     # ran_idx = random.randint(0,len(letters)-1)
#     # password += letters[ran_idx]
#     password +=  random.choice(letters)
#
# for char in range(0, nr_symbols):
#     # idx2 = random.randint(0, len(symbols)-1)
#     # password += symbols[idx2]
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     # idx3 = random.randint(0, len(numbers)-1)
#     # password += numbers[idx3]
#     password += random.choice(numbers)
#
# print(f"Password items : {password}")


# Hard Version

password = [""]

for char in range(0,nr_letters):
    password +=  random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

# my try :
# final_pass = ""
# for char in password:
#     random_num = random.randint(0, len(password)-1)
#     final_pass += password[random_num]

random.shuffle(password)
print(f"Your Password contains : {password}")

pwd = ""
for char in password:
    pwd += char

print(f"Your Password is : {pwd}")
