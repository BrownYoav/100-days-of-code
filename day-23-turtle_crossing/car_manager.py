from turtle import Turtle,Screen
from random import choice,randint

COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
STRETCH_LEN = 2.5
CAR_LEN = 20*STRETCH_LEN
CAR_WIDTH = 30


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.create_car()
        self.moving_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        self.shape('square')
        self.speed('fastest')
        self.right(180)
        self.penup()
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=STRETCH_LEN)
        self.goto(300,randint(-250,280))


    def move(self,level):
        self.forward(self.moving_speed+(level*MOVE_INCREMENT))

    def increase_speed(self):
        self.moving_speed += MOVE_INCREMENT


# screen = Screen()
# screen.setup(width=600, height=600)
# car = CarManager()
#
# screen.exitonclick()