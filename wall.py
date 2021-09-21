from turtle import Turtle
import random

start_x = -460

colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
           "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray", "white"]


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.bricks = []
        self.start_x = start_x

    def create_bricks(self, y):
        for i in range(0, 12):
            self.brick = Turtle("square")
            self.brick.color("white", random.choice(colours))
            self.brick.shapesize(stretch_len=4, stretch_wid=2)
            self.brick.penup()
            # if i == 0:
            #     brick.goto(self.start_x + (i * 80), y)
            # else:
            self.brick.goto(self.start_x + (i * 80), y)
            self.bricks.append(self.brick)

    # def create_middle(self):
    #     for i in range(0, 24):
    #         brick = Turtle("square")
    #         brick.color(random.choice(colours))
    #         brick.shapesize(stretch_len=4, stretch_wid=1)
    #         brick.penup()
    #         brick.goto(self.start_x + (i * 80), self.start_y + 20)
    #         self.bricks.append(brick)
    #
    # def create_bottom(self):
    #     for i in range(0, 24):
    #         brick = Turtle("square")
    #         brick.color(random.choice(colours))
    #         brick.shapesize(stretch_len=4, stretch_wid=1)
    #         brick.penup()
    #         brick.goto(self.start_x + (i * 80), self.start_y + 40)
    #         self.bricks.append(brick)
