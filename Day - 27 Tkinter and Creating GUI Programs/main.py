from tkinter import *

# Window setup
window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Label
my_label = Label(text="Im a Label", font=("Arial",20,"bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(pady=50, padx=50)

# Button
def button_click():
    new_text = input_i.get()
    my_label.config(text=new_text)

button = Button(text="Click Me!", command=button_click)
button.grid(column=1,row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input_i = Entry(width=15)
input_i.grid(column=3, row=2)


# Challenge-1 : Label(col=0,row=0) , button(col=1,row=1) , new_button(col=2, row=0) , entry(col=3, row=2)
# Completed .

# END
window.mainloop()


# my_label.place(x=0, y=0)
# this line shows the label on the window [ .pack() ] -> difficult for precise positioning
# my_label.pack()

#  ways to provide values or change values of a component
# my_label["text"] = "New Text"
# my_label.config(text="Newwww Text 2")