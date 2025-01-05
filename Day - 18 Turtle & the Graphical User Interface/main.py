import random
from turtle import Turtle, Screen

tim = Turtle()

# tim.shape("turtle")
tim.color("blue")

""" Triangle """
# tim.forward(100)
# tim.left(120)
# tim.forward(100)
# tim.left(120)
# tim.forward(100)


""" Challenge - 1 draw a Square """

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)


""" Challenge - 2 Draw a dashed line """
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


"""challenge - 3 Draw Shapes - Triangle, pentagon, hexagon,heptagon, octagon, nonagon, decagon"""
color = ["blue", "green", "red", "yellow","cyan", "pink", "purple", "gray", "brown", "violet", "orange"]

def draw_shape(slides):
    angle = 360/slides
    for _ in range(slides):
        tim.forward(100)
        tim.left(angle)

for shape_slide in range(3, 11):
    tim.color(random.choice(color))
    draw_shape(shape_slide)

screen = Screen()
screen.exitonclick()