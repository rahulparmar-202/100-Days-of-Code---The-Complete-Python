from random import randint
""" original code """
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)   # the index starts from 0 to 5 , so the item 1 will never get displayed
# print(dice_images[dice_num])

""" 1 error that we can produce is 'list index out of range' 
we can do this by using the same randint() method
,that generates a random value from a to b : randint(1, 10) will generate a random number from 1 to 10
then we can make it like : randint(10, 20)
so that it will always generate a number from 10 to 20...
and that index is not available in our list (dice_images).

2. error is that we can make the dice_num a constant value like 8 then,
it will produce the same error everytime.
 """

""" my code """
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(10, 20)
# # this will always cause an error
# print(dice_images[dice_num])

""" to remove the bug """
# randint(0,5)
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0,5)
print(dice_images[dice_num])