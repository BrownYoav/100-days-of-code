from turtle import Screen, Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head: Turtle = self.segments[0]
        self.x = int(self.head.position()[0])
        self.y = int(self.head.position()[1])

    def create_snake(self):
        """creating snake body"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.setposition(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        num_of_segments = len(self.segments)
        last_seg_num = num_of_segments - 1

        for seg_num in range(last_seg_num, 0, -1):
            current_seg = self.segments[seg_num]
            next_seg = self.segments[seg_num - 1]
            current_seg.goto(next_seg.pos())

        self.head.forward(MOVE_DISTANCE)
        self.x = int(self.head.position()[0])
        self.y = int(self.head.position()[1])

    def right(self):
        self.head.right(90)

    def left(self):
        self.head.left(90)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head: Turtle = self.segments[0]
        self.x = int(self.head.position()[0])
        self.y = int(self.head.position()[1])

