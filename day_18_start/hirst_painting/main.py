import random
import turtle as t
# import colorgram as cg
#
# colors = cg.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
t.colormode(255)
tim = t.Turtle()
color_list = [(251, 250, 235), (240, 252, 243), (253, 243, 247), (229, 242, 247), (238, 230, 77), (175, 19, 44), (116, 178, 201), (180, 74, 41), (206, 161, 101), (30, 119, 161), (21, 136, 82), (182, 45, 64), (219, 62, 96), (21, 34, 67), (186, 179, 24), (73, 171, 100), (215, 134, 156), (237, 231, 4), (127, 182, 129), (40, 44, 114), (215, 75, 55), (19, 165, 209), (9, 53, 33), (11, 96, 54), (163, 24, 20), (233, 166, 181), (152, 208, 219), (160, 210, 182), (233, 174, 165), (90, 23, 59)]

tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.speed(10)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = t.Screen()
screen.exitonclick()


