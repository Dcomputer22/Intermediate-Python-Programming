import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
color_list = [(251, 250, 235), (240, 252, 243), (253, 243, 247), (229, 242, 247), (238, 230, 77), (175, 19, 44), (116, 178, 201), (180, 74, 41), (206, 161, 101), (30, 119, 161), (21, 136, 82), (182, 45, 64), (219, 62, 96), (21, 34, 67), (186, 179, 24), (73, 171, 100), (215, 134, 156), (237, 231, 4), (127, 182, 129), (40, 44, 114), (215, 75, 55), (19, 165, 209), (9, 53, 33), (11, 96, 54), (163, 24, 20), (233, 166, 181), (152, 208, 219), (160, 210, 182), (233, 174, 165), (90, 23, 59)]
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

tim.speed("slowest")
def turn_left():
    tim.dot(20, random.choice(color_list))
    tim.left(90)
    tim.penup()
    tim.forward(50)
    tim.left(90)

def turn_right():
    tim.dot(20, random.choice(color_list))
    tim.right(90)
    tim.penup()
    tim.forward(50)
    tim.right(90)


def paint_dots():
    num_of_count = 0
    for _ in range(10):
        for step in range(10):
            random_color = random.choice(color_list)
            tim.color(random_color)
            tim.dot(20, random_color)
            tim.forward(50)
            if step == 9:
                num_of_count += 1
                if num_of_count % 2 != 0:
                    turn_left()
                else:
                    turn_right()

paint_dots()

screen = t.Screen()
screen.exitonclick()