from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        car_chance = random.randint(1,5)
        if car_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    # moves the car backwards with car.speed
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)

    # increase the speed
    def speed_up(self):
        self.speed += MOVE_INCREMENT



