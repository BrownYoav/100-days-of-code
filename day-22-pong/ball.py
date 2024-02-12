import time
from turtle import Turtle, Screen
from config import *
from random import choice
from time import sleep

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.ball_speed = BALL_SPEED



    def move(self):
        self.forward(self.ball_speed)

    def collission_with_ceiling(self):
        """flips the direction on the the Y axis by negating the heading from 360 degrees"""
        ball_direction = self.heading()
        new_heading = 360 - ball_direction
        self.setheading(new_heading)

    def collision_with_paddle(self):
        """calls the collision with ceiling function and also flips the direction on the x axis"""
        ball_direction = self.heading()
        self.collission_with_ceiling()
        self.right(180)

    def create_ball(self):
        self.goto(0,0)
        self.penup()
        self.shape("circle")
        self.color('white')
        self.shapesize(stretch_wid=STRETCH_WIDTH_BALL, stretch_len=STRETCH_LEN_BALL)
        self.speed('fast')
        self.setheading(choice(LIST_OF_BALL_DIRECTIONS))

    def increase_speed(self):
        self.ball_speed += BALL_SPEED_INCREASE_INCREMENT

    def reset_speed(self):
        self.ball_speed = BALL_SPEED


# screen = Screen()
# screen.bgcolor('black')
# screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
# ball = Ball()
# while True:
#     if (Y_BALL_TOP_COORDINATES < ball.position()[1]) or (ball.position()[1] < Y_BALL_BOTTOM_COORDINATES):
#         ball.collide_with_ceiling()
#     else:
#         pass
#     ball.move()
#
# screen.exitonclick()