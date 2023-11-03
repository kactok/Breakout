from ball import Ball
from paddle import Paddle
from blocks import Blocks
from turtle import Screen
from score import Score
import time

# Init game window
screen = Screen()
screen.setup(width=1000,
             height=700)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

# display ball, paddle and blocks on screen
paddle = Paddle()
ball = Ball()
score = Score()
colors = ['yellow', 'green', 'orange', 'red']
# points and speed per color
points_speed = {'yellow': {
    "points": 1,
    "speed": 0
            },
    'green': {"points": 3,
              "speed": .0},
    'orange': {"points": 5,
               "speed": .00001},
    'red': {"points": 7,
            "speed": .00002}}

# All blocks
blocks = []

# number of hits
hit = 0

for value in range(4):
    # next row with different color
    move_up = value * 40
    for new in range(11):
        # add next block in a row
        next = new * 90
        block = Blocks(next, colors[value], move_up)
        blocks.append(block)

# move paddle while key pressed
screen.listen()
screen.onkeypress(key="Left", fun=paddle.go_left)
screen.onkeypress(key="Right", fun=paddle.go_right)

# flag, if True -> game continuous
game_is_on = True

# starting ball speed
speed = .005

while game_is_on:
    screen.update()
    time.sleep(speed)
    ball.move()
    ball.bounce_wall()
    ball.bounce_pad(paddle)
    for block in blocks:
        if block.xcor() - 50 < ball.xcor() < block.xcor() + 50 and (
                block.ycor() + 20 == ball.ycor() or ball.ycor() == block.ycor() - 20):
            ball.value_y *= -1
            speed -= points_speed[block.my_color]['speed']
            score.add_score(points_speed[block.my_color]['points'])
            block.hideturtle()
            blocks.remove(block)
            hit += 1
            speed -= ball.increase_speed(hit)
        elif block.ycor() - 20 < ball.ycor() < block.ycor() + 20 and (
                block.xcor() + 50 == ball.xcor() or ball.xcor() == block.xcor() - 50):
            ball.value_x *= -1
            speed -= points_speed[block.my_color]['speed']
            score.add_score(points_speed[block.my_color]['points'])
            block.hideturtle()
            blocks.remove(block)
            hit += 1
            speed -= ball.increase_speed(hit)
    if ball.ycor() < -330:
        game_is_on = False

screen.exitonclick()
