from turtle import Turtle


class Paddle(Turtle):

    speed = 50
    max_position = 200

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(0, -120)

    def move_left(self):
        self.goto(self.xcor() - self.speed, self.ycor())
        if self.xcor() < self.max_position * -1:
            self.goto(self.max_position * -1, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + self.speed, self.ycor())
        if self.xcor() > self.max_position:
            self.goto(self.max_position, self.ycor())
