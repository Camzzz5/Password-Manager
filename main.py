from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for i in range(randint(8, 10))]
    password_list += [choice(symbols) for i in range(randint(2, 4))]
    password_list += [choice(numbers) for i in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    inp2.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    new_data = {inp1.get():
                    {
                        "email": inp3.get(),
                        "password": inp2.get()
                    }
    }

    if inp1.get() == "" or inp2.get() == "":
        is_yes = messagebox.showinfo(title="Oops", message="Please do not leave any fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        finally:
            inp1.delete(first=0, last=END)
            inp2.delete(first=0, last=END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
canvas = Canvas(height=200, width=200)
window.config(padx=20, pady=20)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo_image)
canvas.grid(row=0, column=1)

inp1 = Entry(width=35)
inp1.grid(column=1, row=1, columnspan=2)
inp3 = Entry(width=35)
inp3.grid(column=1, row=2, columnspan=2)
inp2 = Entry(width=21)
inp2.grid(column=1, row=3)
inp1.focus()
inp3.insert(0, "camilosantander@usantotomas.edu.co")
LABEL1 = Label(text="Website:")
LABEL1.grid(column=0, row=1)
LABEL2 = Label(text="Email/Username:")
LABEL2.grid(column=0, row=2)
LABEL3 = Label(text="Password:")
LABEL3.grid(column=0, row=3)

button1 = Button(text="Add", command=save)
button1.grid(column=1, row=4, columnspan=2)
button1.config(width=35)
button2 = Button(text="Generate Password", command= generate_password)
button2.grid(column=2, row=3)





window.mainloop()