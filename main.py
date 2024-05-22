from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.tracer(0)

ball = Ball()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bouncep()

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()


screen.exitonclick()



