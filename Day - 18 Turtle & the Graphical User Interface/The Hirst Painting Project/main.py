# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import random
import turtle as turtle_module

"""set the color mode to rgb"""
turtle_module.colormode(255)
tim = turtle_module.Turtle()
"""random rgb color list"""
color_list = [(215, 225, 218), (224, 227, 233), (125, 37, 24), (163, 103, 56), (184, 158, 53), (6, 56, 82), (108, 68, 85), (46, 34, 32), (113, 160, 175), (23, 121, 170), (75, 37, 47), (66, 153, 135), (9, 66, 46), (87, 139, 59), (130, 39, 42), (182, 96, 80), (204, 202, 144), (144, 175, 158), (171, 151, 156), (178, 201, 185), (221, 181, 167), (31, 78, 61), (24, 76, 91), (88, 142, 156), (161, 108, 112), (213, 179, 182), (169, 199, 209)]

tim.speed("fastest")
tim.penup()
tim.hideturtle() # this line hides the turtle arrow

"""set its heading to down and forwarding it to the bottom left"""
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# number of dots to be printed
number_of_dots = 100

# included the  + 1 because the range goes till 99
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()