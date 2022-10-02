import random
import turtle 

my_turtle = turtle.Turtle()
my_turtle.pensize(10)
my_screen = turtle.Screen()

def w_key():
    my_turtle.color(random_color())
    my_turtle.forward(40)

def s_key():
    my_turtle.color(random_color())
    my_turtle.backward(40)
    
def a_key():
    my_turtle.color(random_color())
    my_turtle.left(45)
    
def d_key():
    my_turtle.color(random_color())
    my_turtle.right(45)

def c_key():
    my_turtle.color(random_color())
    my_turtle.clear()
    
def space_key():
    my_turtle.color(random_color())
    my_turtle.up()
    
def m_key():
    my_turtle.color(random_color())
    my_turtle.down()



def random_color():
    turtle.colormode(255)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return (R, G, B)



my_screen.listen()
my_screen.onkey(key ="w",fun = w_key)
my_screen.onkey(key ="s",fun = s_key)
my_screen.onkey(key ="a",fun = a_key)
my_screen.onkey(key ="d",fun = d_key)
my_screen.onkey(key ="c",fun = c_key)
my_screen.onkey(key ="space",fun = space_key)
my_screen.onkey(key ="m",fun = m_key)
my_screen.exitonclick()