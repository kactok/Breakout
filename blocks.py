from turtle import Turtle


class Blocks(Turtle):
    """Create a wall of blocks"""
    def __init__(self, next: int, color: str, move_up: int):
        super().__init__()
        self.my_color = color
        self.color(color)
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1.5,
                       stretch_len=4)
        self.goto(x=-455+next, y=150+move_up)

