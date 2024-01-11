from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0),(-40,0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
    
    def create_snake(self):
        for position in STARTING_POSITION:
            new_snake = Turtle('square')
            new_snake.speed(0)
            new_snake.color('white')
            new_snake.penup()
            new_snake.goto(position)
            self.snakes.append(new_snake)
            
    def move(self):
        for num in range(len(self.snakes)-1,0,-1):
            positionX = self.snakes[num -1].xcor()
            positionY = self.snakes[num -1].ycor()
            self.snakes[num].goto(positionX,positionY)
        self. snakes[0].forward(MOVE_DIS)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)