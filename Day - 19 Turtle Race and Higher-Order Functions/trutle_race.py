import turtle
from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

# boolean variable for while loop
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="which turtle win the race? Enter a color : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = [] # list that will contain 6 turtles

y_position = [-100, -60, -20, 20, 60, 100]  # positions for each turtle
""" creating 6 turtle through looping """
for turtle_index in range(0,6):
    new_turtle = Turtle("turtle") # we can shape the turtle when creating its object
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

# is_race_on  variable will be running the while loop of game logic
if user_bet:
    is_race_on = True


while is_race_on:
    # for each turtle we created
    for turtle in all_turtles:
        # if the turtle goes beyond x=230, then race will be stopped
        if turtle.xcor() > 230:
            is_race_on = False
            # .pencolor() returns the first color of the turtle not all the colors
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle is the winner.")
            else:
                print(f"You Lost! the {winning_color} turtle won the race.")
        # created a random distance for each turtle form 0 to 10 and the turtle moves by these random distance.
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()