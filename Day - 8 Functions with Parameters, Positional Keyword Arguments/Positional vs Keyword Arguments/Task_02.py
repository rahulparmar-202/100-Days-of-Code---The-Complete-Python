# Functions with input
# Pause - 1 : Create a function with multiple inputs
def greet_with_name(name,age):
    print(f"Hello {name}, you're {age} right?")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer",19)


# Pause - 2 : Modify the function so that it prints the expected values.
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
#
# greet_with("rahul", "London")


# Keyword Argument :-

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with( location="London", name="rahul")
