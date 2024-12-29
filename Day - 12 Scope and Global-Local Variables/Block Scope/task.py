# Accessible anywhere
anywhere = 1


def my_function():
    # Only accessible inside my_function()
    within_func = 2


for _ in range(10):
    # Accessible anywhere
    my_block_var = 3

print(anywhere)
# print(within_func)  cause an Error
print(my_block_var)

"""Python is a bit different from other programming languages in that it does not have block scope."""

# if we create a variable in a function then it will not be accessed outside the function
# but in block scope(loops, conditionals like if-else) if we create a varibale then it will be accessible even outside the block.