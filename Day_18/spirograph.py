import turtle 
import random


my_turtle =  turtle.Turtle()
my_turtle.speed("fastest")

def random_color():
    turtle.colormode(255)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return (R, G, B)
    
for x in range(1,361,5):
    my_turtle.color(random_color())
    my_turtle.setheading(x)
    my_turtle.circle(100)





my_screen = turtle.Screen()
my_screen.exitonclick()