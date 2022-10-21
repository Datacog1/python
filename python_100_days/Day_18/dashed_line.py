from turtle import Turtle, Screen

my_turtle =  Turtle()

for _ in range(20):
    my_turtle.pendown()
    my_turtle.fd(10)
    my_turtle.penup()
    my_turtle.fd(8)
    
    
my_screen = Screen()
my_screen.exitonclick()