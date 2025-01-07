from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

"""Challenge - 1 : Make an Etch-A-Sketch App [Completed]"""

def move_forward():
    tim.forward(10)

def turn_left():
    tim.setheading(tim.heading() + 10)
    # curr_heading = tim.heading()
    # tim.setheading(curr_heading + 10)

def turn_right():
    tim.setheading(tim.heading() - 10)
    # current_heading = tim.heading()
    # tim.setheading(current_heading - 10)

def move_backwards():
    tim.backward(10)

def clear_screen():
    tim.clear() # clears the screen and not the turtle
    tim.penup() # putting the penup so, it won't draw the path to home
    tim.home()  # turtle goes back to the starting points

    # tim.reset() # this reset's turtle position back to beginning
"""there is also a screen.clear() :-  that clears the whole screen even the turtle"""

screen.listen() # starts listening the keystrokes

# if the key match the respective functions will be called
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right,key="d")
screen.onkey(fun=clear_screen,key="c")



screen.exitonclick()