from turtle import Turtle
from random import *

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.color('blue')
        self.new_pos()

    def new_pos(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.setposition(x=random_x, y=random_y)
