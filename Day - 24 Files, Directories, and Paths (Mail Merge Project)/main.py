# open("file_name.txt", mode="r")
"""r: readonly(default), w:write , a:append (append text without deleting prev one)"""
# file_variable.read()  :- to read the file

# file = open("my_file.txt")
"""with open("my_file.txt") as file:
    contents = file.read()
    print(contents)"""

"""if we use the with open method then we dont hv to close it"""
# file.close()

# 2. writing into a file :>
"""with open("my_file.txt", mode="a") as file:
    file.write("New Text with .write() ")"""


# 3. create a new file :>
"""with open("new_file.txt", mode="w") as file:
    file.write("new text into the new file.")"""
# w mode creates a new file if it doesn't exist.


# 4. read file from the Desktop :> Absolute path (always relative to the root )
"""with open("C:/Users/rahul/Desktop/Day-24.txt", mode="r") as ds_file:
    print(ds_file.read())"""

# 5. read file from Desktop :> Relative Path (always relative to the current folder/file)
with open("../../Desktop/Day-24.txt", mode="r") as r_file:
    print(r_file.read())