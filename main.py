from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    snake_body = Turtle(shape="square")
    snake_body.pu()
    snake_body.color("white")
    snake_body.goto(position)
    segments.append(snake_body)


  
game_is_on  = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    for seg in range(len(segments) - 1, 0, -1):
        new_x = segments[seg - 1].xcor()
        new_y = segments[seg - 1].ycor()
        segments[seg].goto(new_x, new_y)
        
    segments[0].fd(20)
        
        








screen.exitonclick()