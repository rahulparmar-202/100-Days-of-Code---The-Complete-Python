#
# import turtle
# from turtle import Screen
#
# # construct a new object of class Turtle()
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
#
# # color("red") - changes the color of the turtle (timmy here)
# timmy.color("orange")
#
# timmy.forward(100)
#
#
# # creating a Screen object
# my_screen = Screen()
# # .bgcolor("blue") to change the background color
# my_screen.bgcolor("blue")
# print(my_screen.canvheight) # 300
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmender"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# aligns the data (l "left", c "center", r "right")
table.align = "l"

print(table)
