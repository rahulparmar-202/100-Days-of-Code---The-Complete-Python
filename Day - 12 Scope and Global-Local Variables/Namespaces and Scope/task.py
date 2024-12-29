enemies = 1
# Global Variable

def increase_enemies():
    enemies = 2
    # local variable
    print(f"enemies inside function: {enemies}")

friend = 10
# global variable

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope :
# a variable that is created inside a function then it won't be accessible outside the function

# Global Scope :
# a variable that is created outside the function then it will be accessible anywhere in the code


# Namespace :- a system that ensures that all the names (identifiers) in a program are unique to avoid naming conflicts.
# L E G B  Rule:-
# Local
# Enclosing
# Global
# Built-in