from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # update the score and write the score on the screen
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # counts and updates the points for the left player
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # counts and update the points for the right player
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()