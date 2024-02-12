import time
from turtle import Turtle, Screen
from config import *
from time import sleep


class Paddle(Turtle):

    def __init__(self, x_coordinates):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=PADDLE_STRETCH_WIDTH, stretch_len=PADDLE_STRETCH_LEN)
        self.speed('fastest')
        self.goto(x_coordinates, 0)


    def move_up(self):
        if self.position()[1] > Y_PADDLE_TOP_COORDINATES:
            pass
        else:
            self.forward(distance=PADDLE_SPEED)

    def move_down(self):
        if self.position()[1] < Y_PADDLE_BOTTOM_COORDINATES:
            pass
        else:
            self.back(distance=PADDLE_SPEED)


