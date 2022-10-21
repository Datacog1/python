import random
import turtle

walk = turtle.Turtle()

walk.hideturtle()
walk.pensize(15)
walk.speed("fastest")

def random_color():
    turtle.colormode(255)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return (R, G, B)

def turn():
    return random.choice([0, 90, 180, 270])

for _ in range(300):
    walk.color(random_color())
    walk.forward(30)
    walk.setheading(turn())