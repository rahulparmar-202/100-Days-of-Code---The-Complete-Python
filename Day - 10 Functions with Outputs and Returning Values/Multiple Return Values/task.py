def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You Did not provided valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Name : {formated_f_name} {formated_l_name}"


print(format_name(input("What is your First name ?"), input("What is your last name?")))

# take names from inputs then call the function with those values and then print the return from function

