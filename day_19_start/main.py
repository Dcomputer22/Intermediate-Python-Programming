from turtle import Turtle, Screen
tom = Turtle()

def forward():
    tom.forward(15)

def backward():
    tom.backward(15)

def counter_clockwise():
    tom.left(10)


def clockwise():
    tom.right(10)


def clear_drawing():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

def sketch():
    screen.onkey(key="w", fun=forward)
    screen.onkey(key="s", fun=backward)
    screen.onkey(key="a", fun=counter_clockwise)
    screen.onkey(key="d", fun=clockwise)
    screen.onkey(key="c", fun=clear_drawing)


screen = Screen()
screen.listen()
sketch()
screen.exitonclick()
