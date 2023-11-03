from turtle import Turtle


class Score(Turtle):
    """Display score"""

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-400, 300)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Arial", 30, "normal"))

    def add_score(self, value):
        self.clear()
        self.score += value
        self.write(f"Score: {self.score}", align="center", font=("Arial", 30, "normal"))
