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
        """Create snake in middle of the screen joining 3 segments"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self,position):
            snake_body = Turtle(shape="square")
            snake_body.pu()
            snake_body.color("white")
            snake_body.goto(position)
            self.segments.append(snake_body)
            
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        """Function to link snake segments and move snake forward 20 paces"""
        for seg in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg - 1].xcor()
                new_y = self.segments[seg - 1].ycor()
                self.segments[seg].goto(new_x, new_y)
                        
        self.head.fd(MOVE_DISTANCE)
                
    def move_up(self):
        """Snake can move up if not going down"""
        if self.head.heading()!= DOWN:
            self.head.seth(UP)
    
    def move_down(self):
        """Snake can move down if not going up"""
        if self.head.heading()!= UP:
            self.head.seth(DOWN)
        
    def move_left(self):
        """Snake can move left if not going right"""
        if self.head.heading()!= RIGHT:
            self.head.seth(LEFT)
    
    def move_right(self):
        """Snake can move right if not going left"""
        if self.head.heading()!= LEFT:
            self.head.seth(RIGHT)
  