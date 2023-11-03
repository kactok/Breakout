from turtle import Turtle


class Paddle(Turtle):
    """Create a movable paddle controlled by player"""

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.shapesize(stretch_wid=1,
                       stretch_len=8)
        self.penup()
        self.goto(x=0, y=-320)

    def go_right(self):
        """move right"""
        if self.xcor() < 410:
            self.forward(20)

    def go_left(self):
        """move left"""
        if self.xcor() > -410:
            self.backward(20)
