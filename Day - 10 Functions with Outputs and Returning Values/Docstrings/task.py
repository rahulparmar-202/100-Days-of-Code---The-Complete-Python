def format_name(f_name, l_name):
    """
    this
    is now
    a comment
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")
print(formatted_name)
length = len(formatted_name)



# if this multiline comment assigned to a variable then it becomes a String (DocString)
"""
    This
    is a 
    multiline 
    comment
"""


# Ex
myStr = """ This
is a 
multiline 
String 
Now
"""