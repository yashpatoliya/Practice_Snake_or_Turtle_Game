from turtle import Turtle,Screen,colormode
import random
t = Turtle()
t.penup()
t.hideturtle()
t.speed('fastest')
t.setheading(225)
t.forward(400)
t.setheading(0)
colorArray = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6', 
		  '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
		  '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A', 
		  '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
		  '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC', 
		  '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
		  '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680', 
		  '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
		  '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3', 
		  '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF'];
def colors_shapes(num):
    for _ in range(num):
        if _ != 0 and _ % 10 == 0:
            t.setheading(90)
            t.forward(60)
            t.setheading(180)  
            t.forward(600)
            t.setheading(0)
        t.dot(20 , random.choice(colorArray))
        t.forward(60)
            
colors_shapes(100)
   

screen = Screen()
screen.exitonclick()