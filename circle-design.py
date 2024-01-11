from turtle import Turtle,Screen,colormode
from random import randint

t = Turtle()
t.speed(0)
colormode(255)
def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    
    return (r,g,b)

def shaps_circle(num):
    for _ in range(int(360/num)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + num)
    
shaps_circle(5)
screen = Screen()
screen.exitonclick()