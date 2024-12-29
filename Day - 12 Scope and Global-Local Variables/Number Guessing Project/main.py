import art
from random import randint

""" Level for the user to choose from """
EASY_LEVEL = 10
HARD_LEVEL = 5


def high_low(user_guess, number, turns):
    """Takes user_guess and actual number and tells the user if their guess is higher or lower and decrease the turns"""
    if user_guess > number:
        print("Too High..")
        return turns - 1
    elif user_guess < number:
        print("Too Low..")
        return turns - 1
    else :
        print(f"You Guessed Right, The number was {number}")

def game_difficulty():
    """Returns the value of Easylevel and HardLevel based on user choice"""
    level = input("Enter Difficulty 'easy' or 'hard' : ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    """the actual game logic"""
    print(art.logo)
    print("Welcome to Number Guessing Game")
    number = randint(1, 100)
    print("Number is between 1 to 100.")
    guess = 0
    turns = game_difficulty()
    while guess != number:
        print(f"You have {turns} chances to guess.")
        guess = int(input("Your Guess : "))
        turns = high_low(guess, number, turns)
        if turns == 0:
            print("You ran out of lives...🤦‍♂️")
            print(f"The number was {number}")
            return
        elif guess != number:
            print("Guess Again >")


while input("Start a Number Guessing Game, Type 'y' or 'n' : ") == "y":
    print("\n"*5)
    game()
