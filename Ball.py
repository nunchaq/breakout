from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -120)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setheading(45)
        self.speed(1)
        self.move_in_x = 10
        self.move_in_y = 10

    def move(self):
        self.goto(self.xcor() + self.move_in_x, self.ycor() + self.move_in_y)

    def bounce(self, x, y):
        self.move_in_x *= x
        self.move_in_y *= y
