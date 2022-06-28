from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.x = 0

    def create(self):
        chance = random.randint(1,3)
        if (chance ==1):
            car = Turtle()
            car.shape("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move(self, x):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + random.randint(1,10) + x)


