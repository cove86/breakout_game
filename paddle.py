from turtle import Turtle # import Turtle class from turtle module


class Paddle(Turtle):  # define Paddle class inheriting from Turtle

    def __init__(self, position):  # initialise class (with input of position)
        super().__init__()  # initialise super class (Turtle)
        self.shape("square")  # set shape to square
        self.color("white")  # colour to white
        self.shapesize(stretch_len=10, stretch_wid=0.5)   # stretch shape to rectangle
        self.penup()  # stop from drawing
        self.setposition(position)  # set position from passed in position

    def move_left(self):  # define move_left method
        new_x = self.xcor() - 30  # new x = current y - 20
        self.goto(new_x, self.ycor())  # go to new co-ordinates

    def move_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())
