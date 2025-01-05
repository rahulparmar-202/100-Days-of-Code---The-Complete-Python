
""" challenge - 04 : Random Walk """

import random
import turtle as t

tim = t.Turtle()
tim.shape("circle")


# color = ["DeepSkyBlue", "green", "red", "yellow","cyan", "pink", "purple", "gray", "brown", "violet", "orange", "darkOrchid", "IndianRed"]
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

direction = [0, 90, 180, 270]
# speed :- 'fastest' , 'fast' , 'slow' , 'normal', 'slowest'
tim.speed("fastest")

# pensize :- turtle pen size
tim.pensize(10)

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))


screen = t.Screen()
screen.exitonclick()

# Tuples :- ( 1, 6, 39)
# tuples are immutable , means values can not be changed