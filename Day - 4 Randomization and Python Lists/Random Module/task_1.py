import random

# # Importing my_module
import my_module
#
# num = random.randint(0,20)
# print(num)
#
# # printing the variable from my_module
# print(my_module.my_fav_number)

# random_0_to_10 = random.random() * 10
# #  by multiplying by 10 it will generate numbers from 0 to 9 (not 10)
# print(random_0_to_10)

# generate Float Number
# random_float = random.uniform(0, 5)
# print(random_float)


# Pause - 1 Heads or Tails
toss_number = random.randint(0,1)
if toss_number == 0:
    print("Heads")
else :
    print("Tails")