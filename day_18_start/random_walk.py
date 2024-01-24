import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
t.colormode(255)

def color_palette():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

directions = [0, 90, 180, 270]
tim.speed("fastest")
tim.pensize(15)

for each_walk in range(100):
    tim.color(color_palette())
    tim.forward(30)
    tim.setheading(random.choice(directions))





screen = t.Screen()
screen.exitonclick()
