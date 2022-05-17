from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        make_car = Turtle("square")
        make_car.color(COLORS[random.randint(0, 5)])
        make_car.turtlesize(stretch_len=2)
        make_car.penup()
        make_car.goto(300, random.randint(-250, 250))
        make_car.setheading(180)
        self.car_list.append(make_car)

    def move_forward(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
