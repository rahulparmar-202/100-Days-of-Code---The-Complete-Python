"""problem code"""
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

"""
1. error was in the 4th line where the double equals are used instead of = ,
that assigns the value taken through the input() method.
"""

"""solution code"""
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"total_words = {total_words}")
