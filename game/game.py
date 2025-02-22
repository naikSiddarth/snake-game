from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height = 600, width = 600)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(key="Up", fun=snake.Up)
screen.onkey(key="Down", fun=snake.Down)
screen.onkey(key="Left", fun=snake.Left)
screen.onkey(key="Right", fun=snake.Right)

while game_is_on:
    sleep(0.1)
    snake.move()
    screen.update()
    
    #Detect collision with food
    distance = snake.head.distance(food)
    if distance < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update()

    #Detect collision with wall
    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280 :
        scoreboard.reset()
        snake.reset()
    #Detect collision with tail 
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()