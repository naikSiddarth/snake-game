from turtle import Turtle
FONT = ("Arial", 8, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,280)
        self.write(f"Score : {self.score} , High score : {self.highscore}", align="center", font=FONT)

    def update(self):
        self.clear()
        self.write(f"Score : {self.score} High score : {self.highscore}", align="center", font= FONT)

    def reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
        self.score = 0
        self.update()
    
    def increase_score(self):
        self.score += 1
