from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
canvas = Canvas(height=200, width=200)
window.config(padx=20, pady=20)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo_image)
canvas.grid(row=0, column=1)

inp1 = Entry()
inp1.config(width=35)
inp1.grid(column=1, row=1, columnspan=2)
inp3 = Entry()
inp3.config(width=35)
inp3.grid(column=1, row=2, columnspan=2)
inp2 = Entry()
inp2.config(width=21)
inp2.grid(column=1, row=3)

LABEL1 = Label(text="Website:")
LABEL1.grid(column=0, row=1)
LABEL2 = Label(text="Email/Username:")
LABEL2.grid(column=0, row=2)
LABEL3 = Label(text="Password:")
LABEL3.grid(column=0, row=3)

button1 = Button(text="Add")
button1.grid(column=1, row=4, columnspan=2)
button1.config(width=35)
button2 = Button(text="Generate Password")
button2.grid(column=2, row=3)
button2.config(width=14)




window.mainloop()