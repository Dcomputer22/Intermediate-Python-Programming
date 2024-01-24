import random
import turtle as f
tom = f.Turtle()

colors = ["cyan", "firebrick", "medium blue", "lawn green", "magenta", "aquamarine", "sandy brown", "maroon", "purple"]
def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for i in range(number_of_sides):
        tom.forward(100)
        tom.right(angle)


for each_side_n in range(3, 11):
    tom.color(random.choice(colors))
    draw_shape(each_side_n)










screen = f.Screen()
screen.exitonclick()