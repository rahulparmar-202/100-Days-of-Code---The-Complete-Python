from turtle import Turtle

CURRENT_SCORE = 0
MOVE = False
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {CURRENT_SCORE}", MOVE, ALIGNMENT, FONT)

    def score_update(self):
        global CURRENT_SCORE
        CURRENT_SCORE += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", MOVE, ALIGNMENT, ("Arial", 14, "normal"))


# .clear() :- used to clear the screen before updating the score.
# .write() : - to crate a text turtle