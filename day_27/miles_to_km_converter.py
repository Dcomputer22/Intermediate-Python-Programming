from tkinter import *

def converter():
    miles = float(entry.get())
    km = round(miles * 1.609)
    converted.config(text=km)


FONT = ("Times", 20, "normal")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=150, width=400)
window.config(pady=40)

first_label = Label(text="is equal to", font=FONT)
first_label.grid(column=0, row=3)

second_label = Label(text="Miles", font=FONT)
second_label.config(padx=15)
second_label.grid(column=3, row=2)

third_label = Label(text="Km", font=FONT)
third_label.grid(column=3, row=3)

entry = Entry(font=FONT, width=10)
entry.insert(END, string="0")
entry.grid(column=2, row=2)

converted = Label(text="0", font=FONT)
converted.grid(column=2, row=3)

button = Button(text="Calculate", font=("Times", 15), command=converter)
button.grid(column=2, row=4)



window.mainloop()