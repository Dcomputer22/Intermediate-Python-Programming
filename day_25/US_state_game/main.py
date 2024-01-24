import turtle
import pandas

FONT = ("Courier", 12, "normal")
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

guess_states = []
while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/{len(state_list)} States Correct!",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_states = [states for states in state_list if states not in guess_states]
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        guess_states.append(answer_state)
        current_data = data[data["state"] == answer_state]
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(int(current_data.x.iloc[0]), int(current_data.y.iloc[0]))
        state_name.write(answer_state, align="center", font=FONT)
