from turtle import Turtle, Screen
from config import *
from random import choice
from paddle import Paddle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color('white')
        self.shapesize(stretch_wid=STRETCH_WIDTH_BALL, stretch_len=STRETCH_LEN_BALL)
        self.speed('fast')
        self.setheading(60)
        self.goto(L_PADDLE_X_COORDINATES + PADDLE_WIDTH,0)
        # self.setheading(choice(LIST_OF_BALL_DIRECTIONS))

    def move(self):
        self.forward(BALL_SPEED)


    def collide_with_ceiling(self):
        """flips the direction on the the Y axis by negating the heading from 360 degrees"""
        ball_heading = self.heading()
        print(ball_heading)
        if 0 < ball_heading < 90:
            self.right(ball_heading*2)
            print(self.get_heading())
        # elif 90 < ball_heading < 180::
        #     self.left()
        # new_heading = 360 - self.get_heading()
        # print(new_heading)
        # self.setheading(new_heading)

l_paddle = Paddle(L_PADDLE_X_COORDINATES)




screen = Screen()
screen.bgcolor('black')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
ball = Ball()
# while True:
#     if (Y_BALL_TOP_COORDINATES < ball.position()[1]) or (ball.position()[1] < Y_BALL_BOTTOM_COORDINATES):
#         ball.collide_with_ceiling()
#     else:
#         pass
#     ball.move()

screen.exitonclick()