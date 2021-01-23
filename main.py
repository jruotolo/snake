from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from score_board import Scoreboard




screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)
screen.colormode(255)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.turn_left, 'Left')
screen.onkey(snake.turn_right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    if snake.head.distance(food) <= 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
