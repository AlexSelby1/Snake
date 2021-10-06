from turtle import Turtle, Screen
STARTING_POSITIONS  = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]


    def create(self):
        for position in STARTING_POSITIONS:
            snake_body = Turtle(shape="square")
            snake_body.pu()
            snake_body.color("white")
            snake_body.goto(position)
            self.segments.append(snake_body)
    
    def move(self):
            for seg in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg - 1].xcor()
                new_y = self.segments[seg - 1].ycor()
                self.segments[seg].goto(new_x, new_y)
                        
            self.head.fd(MOVE_DISTANCE)
                
    
    def move_up(self):
        if self.head.heading()!= DOWN:
            self.head.seth(UP)
    
    def move_down(self):
        if self.head.heading()!= UP:
            self.head.seth(DOWN)
        
    def move_left(self):
        if self.head.heading()!= RIGHT:
            self.head.seth(LEFT)
    
    def move_right(self):
        if self.head.heading()!= LEFT:
            self.head.seth(RIGHT)
  