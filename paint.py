from turtle import Turtle , Screen

t = Turtle()


screen = Screen()

def move_forward():
    t.forward(10)
    
def move_backward():
    t.backward(10)
    
def move_left():
    new_heading = t.heading() + 10
    t.setheading(new_heading)
    
def move_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)
    
def clear():
    t.home()
    t.clear()


screen.listen()

screen.onkey(move_forward , 'Up')
screen.onkey(move_backward , 'Down')
screen.onkey(move_left , 'Left')
screen.onkey(move_right, 'Right')
screen.onkey(clear, 'c')

screen.exitonclick()