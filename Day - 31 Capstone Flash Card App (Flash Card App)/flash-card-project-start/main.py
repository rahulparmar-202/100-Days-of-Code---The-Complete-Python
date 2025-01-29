from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}

# opens the words_to_learn or french_words CSV
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}

# gets a random words from to_learn list
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=image_front)
    flip_timer = window.after(3000, func=back_card)

# Flipped card
def back_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=image_back)

# when the word is known , it removes from the list and write into words_to_learn.csv
def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# Window object
window = Tk()
window.title("FlashCard")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# timer that flips the card after 3sec
flip_timer = window.after(3000, back_card)

# main front canvas ( front card )
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
image_back = PhotoImage(file="images/card_back.png")
image_front = PhotoImage(file="images/card_front.png")
canvas_image= canvas.create_image(400, 263,image=image_front)
card_title = canvas.create_text(400, 150,font=("Arial", 40, "italic"), text="Title")
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"), text="word")
canvas.grid(column=0, row=0, columnspan=2)

# Button
cross_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_img, highlightthickness=0, border=0, command=next_card)
unknown_btn.grid(column=0, row=1)

check_img = PhotoImage(file="images/right.png")
known_btn = Button(image=check_img, highlightthickness=0, border=0, command=is_known)
known_btn.grid(column=1, row=1)




next_card()
window.mainloop()