# import turtle
# from turtle import Turtle, Screen
# jerry = Turtle()
# print(jerry)
# jerry.shape("turtle")
# jerry.color("red", "blue")
# jerry.forward(80)
# jerry.left(100)
# jerry.forward(100)
# jerry.left(150)
# jerry.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
