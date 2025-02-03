
# we can declare the data-type ,
# so we will know that they accept which data type

# age : int
# name : str

# age : int = it shows that the age should be of type int
# -> bool = shows that the function will return a boolean type
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

print((police_check(23)))