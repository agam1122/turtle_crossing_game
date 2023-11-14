import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
screen.listen()
screen.onkey(fun=turtle.up, key='Up')
screen.onkey(fun=turtle.down, key='Down')

scoreboard = Scoreboard()

# create starting line
starting_line = Turtle()
starting_line.penup()
starting_line.goto(300, -220)
starting_line.pendown()
starting_line.goto(-300, -220)
starting_line.hideturtle()

# write start
start = Turtle()
start.penup()
start.hideturtle()
start.goto(210, -250)
start.write(arg='START', font=("Courier", 24, "normal"))

# create end line
end_line = Turtle()
end_line.penup()
end_line.goto(300, 220)
end_line.pendown()
end_line.goto(-300, 220)
end_line.hideturtle()

# write finish
finish = Turtle()
finish.penup()
finish.hideturtle()
finish.goto(200, 220)
finish.write(arg='FINISH', font=("Courier", 24, "normal"))

new_car = CarManager()

game_is_on = True
while game_is_on:
    sleep_time = 0.1
    time.sleep(sleep_time)
    screen.update()
    new_car.add_car()
    new_car.move()
    if turtle.ycor() > 210:
        time.sleep(1)
        turtle.successful_crossing()
        scoreboard.update_level()
        new_car.random_b -= 1

    # detect collision
    for car in new_car.cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            game_over = Turtle()
            game_over.hideturtle()
            game_over.penup()
            game_over.goto(-90, 0)
            game_over.write(arg='GAME OVER', font=("Courier", 35, "normal"))

screen.exitonclick()
