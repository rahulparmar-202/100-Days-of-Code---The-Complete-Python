from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations  = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    should_continue = True
    f_num = int(input("What is your first number?: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_choice = input("Pick an operation: ")
        s_num = int(input("Whats your second number?: "))
        answer =  operations[operation_choice](f_num, s_num)

        print(f"{float(f_num)} {operation_choice} {float(s_num)} = {float(answer)}")
        choice = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculator: ")

        if choice == 'y':
            f_num = answer
        else:
            should_continue = False
            print("\n" * 10)
            calculator()

calculator()