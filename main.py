import turtle as t
import random

c = t.Turtle()

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b

c.speed('fastest')
c.width(5)
c.penup()
c.goto(-700, -400)



for col in range(18):
    c.color(random_color())
    c.pendown()
    c.begin_fill()
    c.circle(20)
    c.end_fill()
    c.penup()
    c.forward(40)
    c.forward(40)
    c.pendown()







screen = t.Screen()
screen.exitonclick()