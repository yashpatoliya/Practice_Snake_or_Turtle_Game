from turtle import Turtle ,Screen
import random
is_race = False
all_turtles = []
screen = Screen()

screen.setup(width=500,height=400)
user_bet = screen.textinput("Turtle Beting","what is your turtle color ?.")
print(user_bet)
colors = ['red','orange','yellow','green','blue','purple']
positionsY = [-70 ,-40 , -10 , 20  ,50 , 80]

for turtle_index in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230,positionsY[turtle_index])
    all_turtles.append(new_turtle)
    
    
if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race = False
            winnig_color = turtle.pencolor()
            if winnig_color == user_bet:
                print(f"you are won! the {winnig_color} turtle is winner.")
            else:
                print(f"you have lost! the {winnig_color} turtle is winner.")
        random_dis = random.randint(0,10)
        turtle.forward(random_dis)
screen.exitonclick()