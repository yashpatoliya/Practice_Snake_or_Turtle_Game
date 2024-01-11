from turtle import Turtle,Screen
from random import choice

t = Turtle()
colors = ['HotPink' , 'red' , "DarkOliveGreen" , 'MediumBlue' , 'Black', 'PowderBlue', 'SaddleBrown','IndianRed','BlueViolet','Purple','LightSalmon']
t.speed(10)
t.pensize(15)
angles = [90 , 180 ,270 ]

for i in range(200):
    steps = 30
    angle = choice(angles)
    color = choice(colors)
    t.fillcolor(color)
    t.color(color)
    t.setheading(angle)
    t.forward(steps)
    

screen = Screen()
screen.exitonclick()