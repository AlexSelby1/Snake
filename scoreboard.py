from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.write(f"CURRENT SCORE: {self.score}", align="center", font=('Barcade', 10, 'bold'))
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER")
        
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
        
       