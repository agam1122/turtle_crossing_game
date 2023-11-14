from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.random_b = 8

    def add_car(self):
        random_choice = random.randint(1, self.random_b)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-200, 200)
            new_car.goto(x=300, y=random_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            x_position = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(x=x_position, y=car.ycor())

