import time
from player import Player,Screen
from random import randint
from car_manager import CarManager,CAR_LEN, CAR_WIDTH
from scoreboard import ScoreBoard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
PLAYER_LEN = 20
PLAYER_WIDTH = 20
WIDTH_PLAYER_CAR_COLLISION_DISTANCE = PLAYER_WIDTH/2 + CAR_WIDTH/2
LEN_PLAYER_CAR_COLLISION_DISTANCE = PLAYER_LEN/2 + CAR_LEN/2

def setting_up_game(number_of_cars:int):
    list_of_cars = []
    for i in range(number_of_cars):
        random_position = (randint(-200, 250), randint(-250, 280))
        car = CarManager()
        car.goto(random_position)
        list_of_cars.append(car)
    return list_of_cars


def create_car(cars_list: list):
    car = CarManager()
    cars_list.append(car)


def move_cars(cars_list: list,level):
    for car in cars_list:
        car.move(level)
        if car.position()[0] < -(SCREEN_WIDTH/2 + CAR_LEN):
            cars_list.remove(car)

def creating_and_moving_cars(cars_list,level):
    #make sure that it doesn't spawn all the cars at once
    x = randint(1,5)
    if x == 1:
        car = CarManager()
        cars_list.append(car)
    move_cars(cars_list,level)
    return cars_list

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

player = Player()
screen.update()
score = ScoreBoard()

game_is_on = True
list_of_cars = setting_up_game(20)
screen.update()


while game_is_on:
    score.write_level()

    # player movement
    screen.listen()
    screen.onkey(fun=player.move, key="Up")

    #player completes level
    if player.position()[1] > SCREEN_HEIGHT / 2 - PLAYER_LEN:
        player.reset_position()
        score.level += 1


    # create and move the cars during the game
    list_of_cars = creating_and_moving_cars(list_of_cars,score.level)

    #detect collision with player
    for car in list_of_cars:
        player_y = player.position()[1]
        car_y = car.position()[1]
        #car and player are on the same Y coordinates
        if car_y <= player_y <= car_y + WIDTH_PLAYER_CAR_COLLISION_DISTANCE or car_y - WIDTH_PLAYER_CAR_COLLISION_DISTANCE <= player_y <= car_y:
            if player.distance(car) < LEN_PLAYER_CAR_COLLISION_DISTANCE:
                game_is_on = False

    time.sleep(0.1)
    screen.update()
screen.exitonclick()
