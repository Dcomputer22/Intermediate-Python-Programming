from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_info = website_entry.get()
    email_info = email_entry.get()
    password_info = password_entry.get()
    new_data = {
        website_info: {
            "email": email_info,
            "password": password_info,
        }
    }

    if len(website_info) == 0 or len(email_info) == 0 or len(password_info) == 0:
        messagebox.showerror(title="Empty field(s)", message="Please no field should be left empty")
    else:
        try:
            with open("data.json", 'r') as data_file:
                #Read the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the old data with the new one
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            content = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data File Not Found")
    else:
        if website in content:
            email = content[website]['email']
            password = content[website]['password']
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exists!")
# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("My Password Manager")
windows.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=54)
email_entry.insert(0, "fatimaoyiza18@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", fg="white", bg="gray", command=find_password)
search_button.config(padx=30)
search_button.grid(row=1, column=2)

gen_password_btn = Button(text="Generate Password", fg="white", bg="dark red", command=generate_password)
gen_password_btn.grid(row=3, column=2)

add_button = Button(text="Add", width=47, command=save)
add_button.grid(row=4, column=1, columnspan=3)


windows.mainloop()