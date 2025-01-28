import random
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# pyperclip :- a python module that is used to copy to clipboard
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# generates the password and show in the input
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # creating lists for random items for password
    password_letters = [choice(letters) for _ in range(randint(4, 6))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # combining lists to make a single password list
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list) # shuffle the list of password

    # join the password_list by "" so it will become a single string,
    password = "".join(password_list)
    password_in.insert(0,password)

    # copy the password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# take the data and write to a file
def save_password():
    # take values from the inputs
    website = website_in.get()
    email = email_in.get()
    password = password_in.get()

    new_data = {website: {
        "email": email,
        "password": password
    }}

    # when the input are empty or password is too short
    if len(website) == 0 or len(password) <= 3:
        messagebox.showinfo(title="Oops!", message="Filling the information is mandatory.")
    else:
        # Exception Handling
        try:
            # open data.json in read mode
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            # create the data.json in write mode
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the old data with new_data
            data.update(new_data)

            # open data.json and save the data into it
            with open("data.json", "w") as data_file:
                # Saving the updated data to the json file
                json.dump(data, data_file, indent=4)
        finally:
            # delete the values from the inputs ( from 0 to END )
            website_in.delete(0, END)
            password_in.delete(0, END)
            website_in.focus()
            print("Data saved to data.txt ")

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def find_password():
    # takes the input of website
    website = website_in.get().title()
    if len(website) == 0:
        messagebox.showinfo(title="Oops!", message="Filling the information is mandatory.")
    else:
        # Exception Handling
        try:
            # opening the data.json in read mode
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        # exception: when the file does not exist.
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No Data File Found.")
        else:
            # when the site is in the data (data.json)
            if website in data:
                # get the password and email for the site
                password = data[website]["password"]
                email = data[website]["email"]
                messagebox.showinfo(title=website, message=f"Email:  {email} \nPassword:  {password}")
            else:
                messagebox.showerror(title="Error", message=f"No details for the website exist.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# canvas containing the image (logo)
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels - Texts
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entries - Inputs
website_in = Entry(width=30, borderwidth=1)
email_in = Entry(width=48, borderwidth=1)
password_in = Entry(width=30, borderwidth=1)

# to insert text in input (Entry)
email_in.insert(0, "example283@gmail.com")

website_in.grid(column=1, row=1, columnspan=1)
email_in.grid(column=1, row=2, columnspan=2)
password_in.grid(column=1, row=3)

# to have the cursor focus at starting
website_in.focus()

# Buttons
search_button = Button(text="Search", width=13, border=1, command=find_password)
generate_btn = Button(text="Generate Password", command=generate_password, border=1)
add_btn = Button(text="Add", width=42, command=save_password)

search_button.grid(column=2, row=1)
generate_btn.grid(column=2, row=3)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()