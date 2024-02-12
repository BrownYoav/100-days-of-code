from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.speed('fastest')
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

# screen = Screen()
# screen.setup(width=600, height=600)
# turtle =Player()
#
# while True:
#     turtle.move()


# screen.exitonclick()
