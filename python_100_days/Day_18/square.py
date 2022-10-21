from turtle import Turtle, Screen

my_turtle =  Turtle()

for x in range(4):
    my_turtle.fd(100)
    my_turtle.left(90)
    
    
my_screen = Screen()
my_screen.exitonclick()