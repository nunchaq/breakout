from turtle import Turtle
import random


class Brick(Turtle):

    min_value = 50
    max_value = 230

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black", (
            random.randint(self.min_value, self.max_value) / 255,
            random.randint(self.min_value, self.max_value) / 255,
            random.randint(self.min_value, self.max_value) / 255))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.hideturtle()

    def position(self, x, y):
        self.goto(x, y)
        self.showturtle()
