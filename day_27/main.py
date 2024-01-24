def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label

my_label = Label(text="I'm a Label", font=("Arial", 24, "bold"))

# To change label text
# my_label["text"] = "I have changed my text"
# my_label.config(text="I can also use config fxn to change text")
# The pack method is compulsory in order for the label to be displayed
# my_label.place(x=100, y=100)
my_label.grid(column=0, row=0)
my_label.config(padx=30, pady=30)
# my_label.pack()

#Create button

button1 = Button(text="Click me", command=button_clicked)
button2 = Button(text="New Button", command=button_clicked)
# button.pack()
button1.grid(column=1, row=1)
button2.grid(column=2, row=0)
button1.config(pady=10, padx=10)

# Entry class

input = Entry(width=25)
# input.pack()
input.grid(column=3, row=3)


window.mainloop()
