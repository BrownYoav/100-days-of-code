from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from difficulty import Difficulty
import time



SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
game_is_on = True

#setting game difficulty
difficulty = Difficulty()
user_input = input("what difficulty would you like to play at ? 'easy'/'medium'/'hard'/'random': ")
difficulty.set_difficulty(user_input)

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()




while game_is_on:
    screen.update()
    time.sleep(difficulty.game_speed)

    screen.listen()
    screen.onkey(fun=snake.left, key='Left')
    screen.onkey(fun=snake.right, key='Right')

    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 20:
        food.new_pos()
        scoreboard.add_score()
        scoreboard.rewrite_score()
        snake.extend()

    if abs(snake.x) > (SCREEN_WIDTH / 2 - 20):
        scoreboard.reset()
        scoreboard.rewrite_score()
        snake.reset()


    if abs(snake.y) > (SCREEN_HEIGHT / 2):
        scoreboard.reset()
        scoreboard.rewrite_score()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments:
        if snake.head.distance(segment) < 10:
            if segment != snake.segments[0]:
                scoreboard.reset()
                scoreboard.rewrite_score()
                snake.reset()

screen.exitonclick()
