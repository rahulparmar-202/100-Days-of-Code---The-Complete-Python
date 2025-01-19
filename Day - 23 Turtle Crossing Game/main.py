import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# objects of the classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# listen for the keypress
screen.listen()
screen.onkeypress(fun=player.move_forward, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # generate the cars and move the cars
    car_manager.create_cars()
    car_manager.move_car()

    # when the turtle collides with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    # when the turtle(player) gets to the finish line (280)
    if player.at_finish_line():
        player.goto_start()
        scoreboard.level_up()
        car_manager.speed_up()



screen.exitonclick()