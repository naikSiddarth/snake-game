from turtle import Turtle
FONT = ("Arial", 8, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,280)
        self.write(f"Score : {self.score}", align="center", font=FONT)
        
    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font= FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial",20,"bold"))