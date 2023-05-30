from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_continues = True
while game_continues:
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.move()
        snake.inc_score()
        scoreboard.update_score(snake.food_score)
        snake.append_snake()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.head_in_body():
        game_continues = False
        scoreboard.final_message(snake.food_score)


    snake.move()
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")

screen.exitonclick()
