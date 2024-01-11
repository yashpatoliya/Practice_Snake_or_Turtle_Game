from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('snake game')
screen.tracer(0)
snakes = []
game_status = True

food = Food()
snake = Snake()

screen.listen()
screen.onkey(snake.up , 'Up')
screen.onkey(snake.down , 'Down')
screen.onkey(snake.left , 'Left')
screen.onkey(snake.right , 'Right')

while game_status:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
    
screen.exitonclick()