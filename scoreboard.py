from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-280, 250)
        self.hideturtle()


    def increase_level(self):
        self.level +=1

    def update_score(self):
        self.clear()
        self.write("level: "+ str(self.level) )
