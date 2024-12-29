from pyexpat import native_encoding


def greet():
    print("hello")
    print("Rahul")
    print("How are you?")

greet()

# Functions with arguments
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}")

greet_with_name("rahul")
greet_with_name("Alex")