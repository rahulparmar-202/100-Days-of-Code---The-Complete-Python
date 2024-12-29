def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:

# 1. What is the for loop doing?
""" Ans: the for loop is iterating in range from 1 to 20."""

# 2. When is the function meant to print "You got it"?
""" Ans: when the value of i is 20."""

# 3. What are your assumptions about the value of i?
""" Ans: the value of i is increasing starting from 1 to 20."""


"""
The problem in this code was 
    for i in range(1, 20):
since we know that how range method works...it does not include the the ending number (20 here)
so we make it to 21 that means now the range(1,21), so i will have the value 20.
"""