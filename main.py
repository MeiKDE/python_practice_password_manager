from tkinter import *
from tkinter import messagebox  # another module of code
from random import choice, randint, shuffle

import pyperclip  # immediately paste password

FONT_NAME = "Courier"
SIZE = 14


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    # Password Generator Project
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    # how many letters, symbols and numbers
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    # use join method instead on every string
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- UI SETUP
# ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)
# window.minsize(width=600, height=600)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(
    file="/Users/mei/projects/python_practice_password_manager/logo.png"
)

canvas.create_image(100, 100, image=logo_image)
# canvas.pack()
canvas.grid(column=1, row=0)

# ----------------LABELS--------------------#
# Website Label
website_lbl = Label(text="Website:", font=(FONT_NAME, SIZE, "normal"))
# website_lbl.pack()
website_lbl.grid(column=0, row=1)

# Email/Username Label
email_username_lbl = Label(text="Email/Username:", font=(FONT_NAME, SIZE, "normal"))
# email_username_lbl.pack()
email_username_lbl.grid(column=0, row=2)

# Password Label
password = Label(text="Password:", font=(FONT_NAME, SIZE, "normal"))
# password.pack()
password.grid(column=0, row=3)

# ----------------Entries--------------------#
# Website entry
website_entry = Entry(width=35)
# website_tbx.pack()
website_entry.grid(column=1, row=1, columnspan=2, sticky="W")
website_entry.focus()
# Email/Username entry
email_username_entry = Entry(width=35)
# email_username_tbx.pack()
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="W")
email_username_entry.insert(0, "angela@gmail.com")
# Password entry
password_entry = Entry(width=35)
# password_tbx.pack()
password_entry.grid(column=1, row=3)

# ----------------Button--------------------#
# generate password button
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3, sticky="W")


# save website, email and password entries into
# data.txt file
website_input = ""
email_username_input = ""
password_input = ""


def save():
    website_input = website_entry.get()
    # print(f"User website_input: {website_input}")
    email_username_input = email_username_entry.get()
    # print(f"User email_username_input: {email_username_input}")
    password_input = password_entry.get()
    # print(f"User password_input: {password_input}")

    # check the length of website and password entry as validation
    # these fields must be filled.
    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(
            title="Oops",
            message="Please make sure you didn't leave any fields empty",
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website_input,
            message=f"These are the details entered: \nEmail:{email_username_input} \nPassword:{password_input} \n Is it ok to save?",
        )

        # ---------------------------- SAVE ENTRIES ------------------------------- #
        # into a new file

        if is_ok:
            file_name = "data"
            with open(
                f"{file_name}.txt",
                mode="a",
            ) as transport_data:
                transport_data.write(
                    f"{website_input} | {email_username_input} |{password_input}\n"
                )
                # print(f"{website_input} {email_username_input} {password_input} \n")
                # delete entries from entries after save
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# add button
add_btn = Button(text="Add", command=save)
add_btn.grid(column=0, row=4, columnspan=2)


window.mainloop()
