""" challenge - 05 : Make a Spirograph """

import turtle as t
import random

tim = t.Turtle()

"""turtle speed"""
tim.speed('fastest')

""" this defines the colormode to rgb by using (255), and the function randomly chooses a value between 0 to 255"""
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

""" this function draws the spirograph, on the basis of the radius size, 
    divides 360/size_of_gap that returns how many time this loop has to run 
"""
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
"""tim.heading() :- returns the angle, where turtle is heading"""

draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()