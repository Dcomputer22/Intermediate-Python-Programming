import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.up, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_movement()

    #Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect if player reaches finish line
    if player.finished_line():
        scoreboard.level_up()
        player.go_to_start()
        car_manager.increase_speed()

screen.exitonclick()