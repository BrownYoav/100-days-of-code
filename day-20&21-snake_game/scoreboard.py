from turtle import Turtle

STARTING_POSITION = (-120, 260)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.pencolor('white')
        self.penup()
        self.hideturtle()
        self.setposition(STARTING_POSITION)
        self.rewrite_score()

    def add_score(self):
        self.score += 1

    def rewrite_score(self):
        self.clear()
        self.write(arg=f'SCORE IS: {self.score} YOUR HIGH SCORE IS: {self.high_score}', font=('Arial', 15, 'normal'))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

    # def game_over(self):

    def difficulty_easy(self):
        return 'easy'

