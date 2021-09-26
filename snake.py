from turtle import Turtle

x_position = [0, -20, -40]
segments = []
# game_is_on = True


class Snake:
    for turtle_index in range(0, 3):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape("square")
        new_turtle.color("white")
        segments.append(new_turtle)
        new_turtle.goto(x_position[turtle_index], 0)

    def move(self):
        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20)
        segments[0].left(90)