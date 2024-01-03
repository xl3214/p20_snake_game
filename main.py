# TODO: Create a snake body
from food import Food
from snake import Snake
from turtle import Screen
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Kristal's First Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

KEYS = {"Up": snake.up, "Down": snake.down, "Left": snake.left, "Right": snake.right}

# TODO: Control the snake

screen.listen()

for key in KEYS:
    screen.onkey(key=key, fun=KEYS[key])

# TODO: Move the snake
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO: Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # TODO: Create a scoreboard and count scores
        score_board.increase_score()

    # TODO: Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # TODO: Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()


screen.exitonclick()
