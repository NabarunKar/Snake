from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        with open('data.txt') as f:
            hs = f.read()
            hs = int(hs)
        self.high_score = hs
        self.score = 0
        self.color('#F0A500')
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align="center", font=("Courier", 22, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode="w") as f:
                string_hs = str(self.high_score)
                f.write(string_hs)
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()