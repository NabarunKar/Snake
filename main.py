import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Creating the objects

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detecting contact with food object
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
