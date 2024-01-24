import random
from turtle import Turtle, Screen

jenny = Turtle()
jenny.shape("turtle")
jenny.color("red")
# #TODO 1 DRAW A DIFFERENT SHAPES
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]


def create_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        jenny.forward(100)
        jenny.right(angle)

for each_shape in range(3, 11):
    jenny.color(random.choice(colours))
    create_shapes(each_shape)




screen = Screen()
screen.exitonclick()