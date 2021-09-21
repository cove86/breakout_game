from turtle import Turtle  # import Turtle class from turtle module


class Ball(Turtle):  # define Ball class inheriting from turtle class

    def __init__(self):  # initialize class
        super().__init__()  # initialize super class (Turtle)
        self.color("white")  # set colour of ball
        self.shape("circle")  # set shape
        self.shapesize(0.5)
        self.penup()  # pen up to stop drawing
        self.x_move = 10  # set x_move variable
        self.y_move = 10  # set y_move variable
        self.move_speed = 0.05  # set move speed
        self.goto(0, -185)

    def move(self):  # define move method
        new_x = self.xcor() + self.x_move  # set new_x as current x + above x_move
        new_y = self.ycor() + self.y_move  # as above with y
        self.goto(new_x, new_y)  # tells ball to go to new co-ordinates

    def bounce_y(self):  # define bounce_y method
        self.y_move *= -1  # reverses co-ordinates (e.g 10 * -1 = -10 so will move opposite direction
        self.move_speed *= 0.9

    def bounce_x(self):  # as above for x
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):  # define reset_position
        self.goto(0, -185)  # set go to center of screen
        self.move_speed = 0.1  # reset ball speed
        self.bounce_y()  # call bounce_method to send ball back to player
