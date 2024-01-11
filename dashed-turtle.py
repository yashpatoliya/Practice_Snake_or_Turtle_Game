from turtle import Turtle, Screen
from random import choice
t = Turtle()
t.color('HotPink')
colors = ['HotPink' , 'red' , "DarkOliveGreen" , 'MediumBlue' , 'Black', 'PowderBlue', 'SaddleBrown','IndianRed','BlueViolet','Purple','LightSalmon']

for _ in range(10):
    color = choice(colors)
    t.color(color)
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

screen = Screen()
screen.exitonclick()

print("hello")