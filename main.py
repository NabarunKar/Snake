import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
x_position = [0, -20, -40]
segments = []

for turtle_index in range(0, 3):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("square")
    new_turtle.color("white")
    segments.append(new_turtle)
    new_turtle.goto(x_position[turtle_index], 0)



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)












screen.exitonclick()