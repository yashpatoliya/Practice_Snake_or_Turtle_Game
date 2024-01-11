from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.speed('fastest')
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()
    
    def refresh(self):
        positon_x = random.randint(-280,280)
        positon_y = random.randint(-280,280)
        self.goto(positon_x,positon_y)