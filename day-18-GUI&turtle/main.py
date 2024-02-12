from turtle import Turtle, Screen
from random import choice
import colorgram

# colors = colorgram.extract('../day-18-GUI&turtle/image.jpg', 1000)
# numb_colours = len(colors)
# print(numb_colours)
# print(colors)
# list_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tup = (r, g, b)
#     list_colors.append(tup)
# print(list_colors)



def rand_color():
    colors_list = [(227, 236, 230), (198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50), (132, 28, 53),
                   (219, 205, 120), (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53), (184, 141, 158),
                   (132, 182, 145), (48, 56, 99), (180, 97, 107), (56, 35, 22), (68, 130, 106), (98, 118, 166),
                   (82, 148, 159), (221, 175, 187), (169, 206, 166), (90, 151, 96), (185, 97, 80), (163, 200, 213),
                   (179, 188, 211), (80, 70, 39), (131, 37, 27), (45, 73, 76), (219, 177, 170), (24, 43, 43),
                   (49, 88, 21)]
    return choice(colors_list)
def draw_circle(size,color):
    tim.color(color)
    tim.begin_fill()
    tim.circle(size)
    tim.end_fill()

def draw_row(numb_circles_inrow):
    for circle in range(numb_circles_inrow):
        draw_circle(20, rand_color())
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.back(50*numb_circles_inrow)


def draw_image(numb_rows,numb_circles_inrow):
    for row in range(numb_rows):
        draw_row(numb_circles_inrow)
        tim.penup()
        tim.left(90)
        tim.forward(50)
        tim.right(90)
        tim.pendown()


tim = Turtle()
tim.speed('fastest')
screen = Screen()
screen.colormode(255)

#start position
tim.penup()
tim.setpos(-250, -250)
tim.pendown()
draw_image(10,10)



screen.exitonclick()
