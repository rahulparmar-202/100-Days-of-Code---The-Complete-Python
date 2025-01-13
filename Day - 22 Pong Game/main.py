from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

# screen settings
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("The Pong Game")
screen.tracer(0)

# created paddle objects
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))

# ball object
ball = Ball()

# scoreboard object for showing the score
scoreboard = ScoreBoard()

# listening for keypress
screen.listen()

# calling functions on each keypress
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

# screen.onkey(fun=r_paddle.go_up, key="Up")
# screen.onkey(fun=r_paddle.go_down, key="Down")
# screen.onkey(fun=l_paddle.go_up, key="w")
# screen.onkey(fun=l_paddle.go_down, key="s")

# game logic

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with walls (top and bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detects R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detects L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()