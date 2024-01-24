from turtle import Turtle, Screen
import random

start_race = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt= "Which turtle color do you think will win the race?: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []
for turtle_positioning in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_positioning])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_positioning])
    all_turtles.append(new_turtle)

if user_bet:
    start_race = True

while start_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            start_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winner is the {winning_color} turtle 😎")
            else:
                print(f"You've lost! The winner is the {winning_color} turtle 🤣")
        rand_movement = random.randint(0, 10)
        turtle.forward(rand_movement)


screen.exitonclick()