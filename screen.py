from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scores = Scoreboard()


def game_exit():
    global game_is_on
    game_is_on = False
    ball.game_over()


screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
screen.onkey(game_exit, 'x')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with upper or lower wall
    if not (-280 < ball.ycor() < 280):
        ball.bounce_y()

    # #   detect when paddle miss ball
    # if not (-350 < ball.xcor() < 350):
    #     ball.game_over()
    #     game_is_on = False

    # Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scores.l_point()

    # Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scores.r_point()

    #   detect collision with right paddle
    if (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50) and not (320 <= ball.xcor() <= 320):
        ball.bounce_x()


screen.exitonclick()
