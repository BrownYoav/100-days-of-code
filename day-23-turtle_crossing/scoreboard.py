from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.speed('fastest')
        self.penup()
        self.setposition(150, 250)

    def write_level(self):
        self.clear()
        self.write(arg=f'LEVEL: {self.level}',font=FONT)

