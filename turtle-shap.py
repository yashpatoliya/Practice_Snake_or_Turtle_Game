from turtle import Turtle,Screen
from random import choice

t = Turtle()
slide =10

colors = ['HotPink' , 'red' , "DarkOliveGreen" , 'MediumBlue' , 'Black', 'PowderBlue', 'SaddleBrown','IndianRed','BlueViolet','Purple','LightSalmon']

def draw_right(num):
    angle = 360 / num
    for _ in range(num):
        color = choice(colors)
        t.color(color)
        t.forward(100)
        t.right(angle)
        
def draw_left(num):
    angle = 360 / num
    for _ in range(num):
        color = choice(colors)
        t.color(color)
        t.forward(100)
        t.left(angle)
        
def draw_top(num):
    angle = 360 / num
    for _ in range(num):
        color = choice(colors)
        t.color(color)
        t.right(angle)
        t.forward(100)
        
def draw_bottom(num):
    angle = 360 / num
    for _ in range(num):
        color = choice(colors)
        t.color(color)
        t.left(angle)
        t.forward(100)

for i in range(3,11):
    draw_right(i)
    draw_left(i)
    draw_top(i)
    draw_bottom(i)
    


screen = Screen()
screen.exitonclick()
