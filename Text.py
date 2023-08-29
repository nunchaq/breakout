from turtle import Turtle


class Text(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 0)

    def game_over(self):
        self.showturtle()
        self.write("GAME OVER", False, align="center", font=("Arial", 35, "normal"))
