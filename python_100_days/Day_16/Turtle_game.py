from re import A
from turtle import Turtle, Screen
timmy = Turtle()
timmy.color("green")

# Screen() is the class and my_screen is object
my_screen = Screen()
my_screen.bgcolor("azure")

timmy.shape("turtle")
timmy.shapesize(7,7,4)
timmy.pencolor("black")
timmy.fd(20)
timmy.pendown()
timmy.left(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(60)
timmy.right(90)
timmy.forward(50)
timmy.right(90)
timmy.forward(60)
timmy.left(180)
timmy.forward(60)
timmy.right(90)
timmy.forward(100)

my_screen.delay(20)
my_screen.bgcolor("azure")
my_screen.exitonclick()
