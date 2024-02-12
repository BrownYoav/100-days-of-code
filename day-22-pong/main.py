import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from config import *
from ball import Ball

game_on = True
screen = Screen()
screen.bgcolor('black')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

l_paddle = Paddle(L_PADDLE_X_COORDINATES)
r_paddle = Paddle(R_PADDLE_X_COORDINATES)

ball = Ball()
ball_speed = BALL_SPEED

l_score = Scoreboard(L_SCORE_POSITION)
r_score = Scoreboard(R_SCORE_POSITION)

screen.update()

while game_on:
    screen.listen()
    # paddle controls
    screen.onkey(fun=l_paddle.move_up, key='w')
    screen.onkey(fun=l_paddle.move_down, key='s')
    screen.onkey(fun=r_paddle.move_up, key='Up')
    screen.onkey(fun=r_paddle.move_down, key='Down')

    # ball movement
    ball.move()

    # ball collisions with ceiling
    if (Y_BALL_TOP_COORDINATES < ball.position()[1]) or (ball.position()[1] < Y_BALL_BOTTOM_COORDINATES):
        ball.collission_with_ceiling()
        ball.increase_speed()
    # ball in certain distance from paddle only when has close x coordinates
    ball_x_position = ball.position()[0]
    if ball_x_position < L_PADDLE_X_COORDINATES + PADDLE_WIDTH or ball_x_position > R_PADDLE_X_COORDINATES - PADDLE_WIDTH:
        if r_paddle.distance(ball) < HIT_DISTANCE_FROM_PADDLE or l_paddle.distance(ball) < HIT_DISTANCE_FROM_PADDLE:
            ball.collision_with_paddle()
            ball.increase_speed()

    # scoring a goal
    if abs(ball_x_position) > SCREEN_WIDTH / 2:
        ball.create_ball()
        ball.reset_speed()
        if ball_x_position < 0:
            r_score.increase_score()
        else:
            l_score.increase_score()
        screen.update()
        time.sleep(1)
        #game finishes
        if l_score.score > MAX_GOALS or r_score.score > MAX_GOALS:
            game_on =False
            print("GAME OVER")
            if r_score.score > MAX_GOALS:
                print("RIGHT PLAYER WON!!!!")
            else:
                print('LEFT PLAYER WON!!!!')

    screen.update()

screen.exitonclick()
