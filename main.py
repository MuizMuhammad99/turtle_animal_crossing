import random

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.title("car-crossing")
screen.tracer(0)
scoreboard = Scoreboard()
turtle = Player()
cars = CarManager()
game_on = True
screen.listen()
screen.onkey(turtle.move, "w")

while game_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_score()
    cars.create()
    cars.move(0)

    for x in cars.cars:
        if (turtle.distance(x) < 10):
            game_on = False
    if turtle.ycor() >= 280:
        turtle.goto(0, -280)
        scoreboard.increase_level()
        cars.x +=5

screen.exitonclick()