from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.level=0
    def update_score(self):
        self.clear()
        self.goto(-285,260)
        self.write(f"Level:{self.level} ", align="Left", font=(FONT))
    def level_up(self):
        self.level +=1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER ", align="Left", font=(FONT))

