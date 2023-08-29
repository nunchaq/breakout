import time
from turtle import Screen
from Ball import Ball
from Brick import Brick
from Paddle import Paddle
from Text import Text

paddle = Paddle()
ball = Ball()
brick = Brick()
text = Text()

screen = Screen()
screen.title("Breakout Clone")
screen.bgcolor("black")
screen.setup(width=500, height=400)
screen.tracer(0)
screen.listen()
screen.onkey(key="Left", fun=paddle.move_left)
screen.onkey(key="Right", fun=paddle.move_right)

wall = []
for i in range(8):
    for j in range(10):
        brick = Brick()
        brick.position(-200 + j * 45, 195 - i * 25)
        wall.append(brick)

game_in_progress = True
while game_in_progress:
    time.sleep(0.1)
    screen.update()
    ball.move()

    for brick in wall:
        if ball.distance(brick) < 50 and ball.ycor() - brick.ycor() < 30:
            ball.bounce(1, -1)
            brick.hideturtle()
            wall.remove(brick)

    if ball.ycor() > 195:
        ball.bounce(1, -1)

    if ball.xcor() > 220 or ball.xcor() < -220:
        ball.bounce(-1, 1)

    if ball.distance(paddle) < 50 and ball.ycor() == -120:
        ball.bounce(1, -1)

    if ball.ycor() < -160 or len(wall) == 0:
        game_in_progress = False
        text.game_over()


screen.exitonclick()
