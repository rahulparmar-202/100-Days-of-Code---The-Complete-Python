from tkinter import *


window = Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# convert the miles to kilometer
def calculate_km():
    miles = miles_in.get()
    # calculating the km and round to 2
    km = (float(miles) * 1.609).__round__(2)
    kilometer_value.config(text=km)

# Entry
miles_in = Entry(width=5, font=('Arial', 10, 'bold'))
miles_in.insert(END, string="0")
miles_in.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles ", font=('Arial', 10, 'bold'))
is_equal_label = Label(text="is equal to ", font=('Arial', 10, 'bold'))
km_text_label = Label(text="Km", font=('Arial', 10, 'bold'))
# texts
miles_label.grid(column=2, row=0)
is_equal_label.grid(column=0, row=1)
km_text_label.grid(column=2, row=1)

# kilometer value
kilometer_value = Label(text="0", font=('Arial',10,'bold'))
kilometer_value.grid(column=1, row=1)
kilometer_value.config(padx=5, pady=5)

# button
button = Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=3)



# Keep the Screen
window.mainloop()