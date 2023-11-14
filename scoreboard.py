from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-270, 270)
        self.write(arg=f"Level: {self.level}", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", font=FONT)