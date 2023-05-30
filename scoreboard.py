from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.sety(260)
        self.update_score()

    def update_score(self, score=0):
        self.clear()
        self.write(f"Current Score: {score}", align="center", font=("Arial", 25, "normal"))

    def final_message(self, score):
        self.clear()
        self.write(f"You lose, Final score: {score}", align="center", font=("Arial", 25, "normal"))

