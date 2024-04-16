from turtle import Turtle

STEP = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake = []
        self.x = 20
        self.y = 0
        self.build_snake()
        self.head = self.snake[0]
        self.prev_last_pos = ()
        self.speed = 0.25

    def speed_up(self):
        if self.speed != 0.5:
            self.speed -= 0.01

    def create_snake_part(self):
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.teleport(x=int(self.prev_last_pos[0]), y=int(self.prev_last_pos[1]))
        self.x -= 20
        self.snake.append(snake_part)

    def build_snake(self):
        for i in range(3):
            snake_part = Turtle(shape="square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.teleport(x=self.x, y=self.y)
            self.x -= 20
            self.snake.append(snake_part)

    def snake_reset(self):
        for part in self.snake:
            part.teleport(800, 800)

        self.x = 20
        self.y = 0
        self.snake.clear()
        self.build_snake()
        self.head = self.snake[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        for index in range(len(self.snake) - 1, 0, -1):
            if index == len(self.snake) - 1:
                self.prev_last_pos = self.snake[index].pos()
            self.snake[index].goto(self.snake[index - 1].xcor(), self.snake[index - 1].ycor())

        self.head.forward(STEP)

