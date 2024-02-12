from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)

def clear():
    screen.reset()

def backwards():
    tim.back(10)

screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='s', fun=backwards)
screen.onkeypress(key='c', fun=clear)




screen.exitonclick()
