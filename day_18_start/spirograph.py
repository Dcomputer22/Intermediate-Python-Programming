import  turtle as t
import random
tim = t.Turtle()
t.colormode(255)

def color_palette():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.speed("fastest")

def draw_circle(num_of_gaps):
    for circle in range(int(360 / num_of_gaps)):
        tim.color(color_palette())
        tim.setheading(tim.heading() + num_of_gaps)
        tim.circle(100)

draw_circle(5)


screen = t.Screen()
screen.exitonclick()
