from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.showturtle()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.back(MOVE_DISTANCE)

    def successful_crossing(self):
        self.goto(STARTING_POSITION)

