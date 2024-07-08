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
    screen.update()
    sleep(0.2)
    snake.move()
    
    #Detect collision with food
    distance = snake.head.distance(food)
    if distance < 12:
        food.refresh()
        

screen.exitonclick()