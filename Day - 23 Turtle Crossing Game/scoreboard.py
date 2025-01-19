from turtle import Turtle

FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-210, 260)
        self.update_scoreboard()

    # updates the scoreboard by writing the current level
    def update_scoreboard(self):
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    # writes the game over text
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", move=False, align="center", font=FONT)

    # clear the screen and updates the level by 1
    def level_up(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()