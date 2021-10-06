from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.goto(position)

    










screen.exitonclick()