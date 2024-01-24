from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()

screen.tracer(0)
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("MY PONG GAME")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.increase_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with both paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when R paddle misses
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()
    #Detect when L paddle misses
    if  ball.xcor() < - 400:
        ball.reset_ball()
        scoreboard.r_point()

    if scoreboard.r_score > scoreboard.l_score and scoreboard.r_score == 5:
        game_on = False
        scoreboard.game_over()

    elif scoreboard.l_score > scoreboard.r_score and scoreboard.l_score == 5:
        game_on = False
        scoreboard.game_over()


screen.exitonclick()