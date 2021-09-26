from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color('#F0A500')
        self.goto(0, 270)

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align="center", font=("Courier", 22, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 22, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()