from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.pu()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"CURRENT SCORE: {self.score}  HIGH SCORE: {self.high_score}", align="center", font=('Barcade', 10, 'bold'))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
        
       