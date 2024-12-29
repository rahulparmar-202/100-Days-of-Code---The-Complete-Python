""" problem code """
# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")

"""
1. error was the print indentation
2. the age > 18 so if the age is equal to 18 then it would not print anything.
3. in the print there was no f string that could take the variable age.

"""

"""solution code"""
# age = int(input("How old are you?"))
# if age >= 18:
#     print(f"You can drive at age {age}.")

""" Try - Except """

try:
    age = int(input("What is your age?: "))
except ValueError:
    print("You have entered an invalid number. Please enter a numerical number like 10.")
    age = int(input("Whats your age again?? "))

if age >= 18:
    print(f"You can drive at age {age}.")