print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("where do you want to go ? \n\tType 'left' or 'right' \n").lower()

if direction == 'left':
    swim_or_not = input("there's a River. How would you like to go on? wait for Boat or Swim\n\tType 'wait' or 'swim'\n").lower()
    if swim_or_not == "swim":
        print("Ohhh! a crocodile killed you. Game Over.")
    elif swim_or_not == 'wait':
        door_color = input("You came across the river, now there are 3 doors - Red, Blue, Yellow. \n\tType 'red' , 'blue' or 'yellow' \n").lower()
        if door_color == "red" :
            print("There is Fire! you died, Game Over.")
        elif door_color == "blue":
            print("hell! its Ice I'm freezed, Game Over.")
        elif door_color == 'yellow':
            print("Congrats! You Won Treasure.")
        else :
            print("You typed Wrong!")
    else :
        print("You typed Wrong!")

elif direction == "right":
    print("You fall of cliff, Game Over.")
else :
    print("You Typed Wrong!")
