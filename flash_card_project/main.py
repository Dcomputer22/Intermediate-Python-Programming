from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/igbo_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/igbo_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient='records')


def next_word():
    global current_card, flip_timer
    windows.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    word = current_card["Igbo"]
    canvas.itemconfig(card_title, text="Igbo", fill="black")
    canvas.itemconfig(card_word, text=word, fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = windows.after(3000, flip_card)


def flip_card():
    word = current_card["English"]
    canvas.itemconfig(card_background, image=back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word, fill="white")


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


windows = Tk()
windows.title("Flash Cards in Igbo")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = windows.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_word)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_word()

windows.mainloop()
