programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop":"The action of doing something over and over again."
}

# # printing a value by its key
# print(programming_dictionary["Loop"])
#
# # dictionary inbuilt functions to get keys and values
# print(programming_dictionary.keys())
# print(programming_dictionary.values())
#
# # adding new key:value pair in dictionary
# programming_dictionary["int"] = "the whole numbers like 2,4,19,694 etc."
# print(programming_dictionary["int"])
#
# # edit a value in dictionary
# programming_dictionary["Bug"] = "A moth in your Computer"
# print(programming_dictionary["Bug"])

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])