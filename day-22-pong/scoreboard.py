from turtle import Turtle,Screen
from config import *

class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.pencolor('white')
        self.speed('fastest')
        self.penup()
        self.setposition(position)
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(arg=f'{self.score}', font=('Times New Roman', 50, 'normal'))

    def increase_score(self):
        self.score += 1
        self.write_score()



# screen = Screen()
# screen.bgcolor('black')
# screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
# # ball = Ball()
# l_score = Scoreboard(L_SCORE_POSITION)
# r_score = Scoreboard(R_SCORE_POSITION)
# # while True:
# #     if (Y_BALL_TOP_COORDINATES < ball.position()[1]) or (ball.position()[1] < Y_BALL_BOTTOM_COORDINATES):
# #         ball.collide_with_ceiling()
# #     else:
# #         pass
# #     ball.move()
# #
# screen.exitonclick()