import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(370)
player=Player()
score=Scoreboard()
score.update_score()
player.create_player()
cars=CarManager()

screen.listen()
screen.onkey(player.up ,"Up")
game_is_on = True
while game_is_on:
    cars.create_car()
    cars.move()
    if player.ycor() > 300:
        score.level_up()
        cars.next_level()
        player.reset()
    for car in cars.all_cars:
        if car.distance(player) <10:
            score.game_over()
            game_is_on= False


    time.sleep(0.1)
    screen.update()

screen.exitonclick()
