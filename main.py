from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
game_is_on = True

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="d", fun=snake.right)

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="w", fun=snake.up)

screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="a", fun=snake.left)

screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="s", fun=snake.down)

while game_is_on:
    screen.update()
    time.sleep(snake.speed)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.create_snake_part()
        snake.speed_up()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.snake_reset()

    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset_score()
            snake.snake_reset()


screen.exitonclick()
