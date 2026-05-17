import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b

c = t.Turtle()
t.colormode(255)
c.hideturtle()

c.speed('fastest')
c.penup()
c.goto(-400, -350)


for row in range(10):
    for col in range(10):
        c.pendown()
        c.dot(40, random_color())
        c.penup()
        c.forward(80)
    c.penup()
    c.goto(-400, -350 + (row + 1) * 80)



screen = t.Screen()
screen.exitonclick()