from turtle import Turtle, Screen
import random

colours = ["olive","red","teal","khaki","orange","navy","blueviolet"]
my_turtle =  Turtle()

def shapes(num_side):
    angle = 360 / num_side
    for _ in range(num_side): 
         my_turtle.forward(100)
        
         ##print(x)
         my_turtle.left(angle)
 
     
for num in range(3,11):
    my_turtle.color(random.choice(colours))
    shapes(num)
    
 

  
my_screen = Screen()
my_screen.exitonclick()