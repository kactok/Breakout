from turtle import Turtle


class Ball(Turtle):
    """Create a ball that bounce once touched"""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.value_x = 1
        self.value_y = -1

    def move(self):
        """Ball movement"""
        new_cor_x = self.xcor() + self.value_x
        new_cor_y = self.ycor() + self.value_y
        self.goto(x=new_cor_x, y=new_cor_y)

    def bounce_wall(self):
        """Bounce of wall"""
        if self.xcor() == 490 or self.xcor() == -490:
            self.value_x *= -1
        if self.ycor() == 320:
            self.value_y *= -1

    def bounce_pad(self, pad: Turtle):
        """Bounce of paddle"""
        if pad.xcor() <= self.xcor() < pad.xcor() + 95 and self.ycor() == pad.ycor() + 20 and self.value_x > 0:
            self.value_y *= -1
        elif pad.xcor() <= self.xcor() < pad.xcor() + 95 and self.ycor() == pad.ycor() + 20 and self.value_x < 0:
            self.value_y *= -1
            self.value_x *= -1
        elif pad.xcor() - 95 < self.xcor() < pad.xcor() and self.ycor() == pad.ycor() + 20 and self.value_x < 0:
            self.value_y *= -1
        elif pad.xcor() - 95 < self.xcor() < pad.xcor() and self.ycor() == pad.ycor() + 20 and self.value_x > 0:
            self.value_y *= -1
            self.value_x *= -1

    def increase_speed(self, hit: int):
        if hit % 12 == 0 and hit != 0:
            return 0.00002
        elif hit % 4 == 0 and hit != 0:
            return 0.0001
        else:
            return 0
