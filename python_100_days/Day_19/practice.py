import imp
from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()

def move():
    my_turtle.forward(10)



my_screen.listen()
my_screen.onkey(key ="space",fun = move)
my_screen.exitonclick()