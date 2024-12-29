# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# ex-2

number = 100

def myfun():
    # number = 200
    # to change the global variable number we use global keyword
    global number
    number = 99
    print("Inside function : " , number)
#     will print 99

myfun()
print("Outside function : " , number)
# number is 99 now