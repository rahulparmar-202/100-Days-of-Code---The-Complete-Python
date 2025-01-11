from turtle import Screen
import  time
from scoreboard import ScoreBoard
from snake import Snake
from food import Food

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# created an object of class Snake
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# listening keypress
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# running the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh() # to refresh the food when it collides with snake
        scoreboard.score_update()  # updates the score
        snake.extend()

    # collision with the wall
    x_cor  = snake.head.xcor()
    y_cor = snake.head.ycor()
    if x_cor > 280 or x_cor < -280 or y_cor > 280 or y_cor < -280:
        game_is_on = False
        scoreboard.game_over()

    # collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Exit
screen.exitonclick()