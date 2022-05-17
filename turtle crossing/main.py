import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
loop_number = 0
car_manager = CarManager()

screen.listen()
player = Player()
scoreboard = Scoreboard()
screen.onkey(player.up, "Up")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_forward()
    loop_number += 1
    if loop_number == 6:
        car_manager.make_car()
        loop_number = 0

    for car in car_manager.car_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.at_finish():
        car_manager.increase_speed()
        scoreboard.increase_level()


screen.exitonclick()
