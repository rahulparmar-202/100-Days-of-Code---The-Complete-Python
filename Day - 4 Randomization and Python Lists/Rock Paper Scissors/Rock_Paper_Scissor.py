import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# computer choice generation with random
computer_choice = random.randint(0,2)

choices = [rock, paper, scissors]
print("Welcome to Rock Paper Scissors Game.")
# User's input choice
user_choice = int(input("Your Choice ? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

user = choices[user_choice]
computer = choices[computer_choice]

# Printing User Choice
print("User's Choice : " )
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else :
    print("Please enter a valid choice !")

# Printing Computer Choice
print("Computer's Choice : ")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

# Game Logic
if user == rock:
    if computer == rock:
        print("Draw.")
    elif computer == paper:
        print("You Lose.")
    elif computer == scissors:
        print("You Won.")
elif user == paper:
    if computer == rock:
        print("You Won")
    elif computer == paper:
        print("Draw")
    elif computer == scissors:
        print("You Lose.")
elif user == scissors:
    if computer == rock:
        print("You Lose.")
    elif computer == paper:
        print("You Won.")
    elif computer == scissors:
        print("Draw")
else:
    print("there might be an error :(")