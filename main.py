from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from wall import Wall

screen = Screen()
screen.screensize(500, 400)
screen.bgcolor("black")
screen.title("Breakout")
screen.listen()
screen.tracer(0)

start_y = 240

paddle = Paddle((0, -195))
ball = Ball()
wall = Wall()
score = Scoreboard()

wall.create_bricks(start_y + (score.level * 20))

# screen.onkeypress(paddle.move_left, "Left")
# screen.onkeypress(paddle.move_right, "Right")

game_is_on = True  # define variable as True

while game_is_on:  # while loop, while above is True
    time.sleep(ball.move_speed)  # set screen sleep based on move_speed from ball object
    screen.update()  # update screen
    ball.move()  # call move method from ball object

    screen.onkeypress(paddle.move_left, "Left")
    screen.onkeypress(paddle.move_right, "Right")

    # Collision with wall
    if ball.ycor() > 260:
        # needs to bounce
        ball.bounce_y()  # call bounce_y method from ball object

    if ball.xcor() > 465 or ball.xcor() < -465:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 100 and ball.ycor() < -185:
        ball.bounce_y()  # call bounce_y method from object

    if ball.ycor() < -210:
        score.update_lives()
        if score.lives >= 1:
            ball.reset_position()
        else:
            score.reset()
            game_is_on = False
            print("Game Over")

    for brick in wall.bricks:
        if brick.distance(ball) < 40:
            ball.bounce_y()
            score.score += 10
            score.update_scoreboard()
            brick.hideturtle()
            wall.bricks.remove(brick)
            # print(f"length of bricks = {len(wall.bricks)}")

    if len(wall.bricks) == 0:
        score.update_level()
        ball.reset_position()

        for i in range(0, score.level):
            # print(f"level = {level}")
            wall.create_bricks(start_y + (i * 40))
            # print(i * 20)


screen.exitonclick()

